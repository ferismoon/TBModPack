import java.nio.file.*;
import java.util.*;
import java.util.zip.*;
import jdk.internal.org.objectweb.asm.*;

// Disables only the redundant loot replacement registration. KubeJS supplies
// the same eight JSON tables; all other Cozy Core classes/resources are retained.
public class PatchCozy {
    public static void main(String[] args) throws Exception {
        Path input = Path.of(args[0]), output = Path.of(args[1]);
        String target = "net/cozystudios/cozystudioscore/CozyStudiosCore.class";
        int[] removed = {0};
        try (ZipFile source = new ZipFile(input.toFile());
             ZipOutputStream out = new ZipOutputStream(Files.newOutputStream(output, StandardOpenOption.CREATE_NEW))) {
            for (var entries = source.entries(); entries.hasMoreElements();) {
                ZipEntry entry = entries.nextElement();
                byte[] bytes;
                try (var stream = source.getInputStream(entry)) { bytes = stream.readAllBytes(); }
                if (entry.getName().equals(target)) {
                    ClassReader reader = new ClassReader(bytes);
                    ClassWriter writer = new ClassWriter(reader, 0);
                    reader.accept(new ClassVisitor(Opcodes.ASM8, writer) {
                        public MethodVisitor visitMethod(int access, String name, String desc, String sig, String[] exceptions) {
                            return new MethodVisitor(Opcodes.ASM8, super.visitMethod(access, name, desc, sig, exceptions)) {
                                public void visitMethodInsn(int opcode, String owner, String method, String descriptor, boolean itf) {
                                    if (opcode == Opcodes.INVOKESTATIC && owner.equals("net/cozystudios/cozystudioscore/loot/LootTableFixes") && method.equals("register") && descriptor.equals("()V")) {
                                        removed[0]++;
                                        return;
                                    }
                                    super.visitMethodInsn(opcode, owner, method, descriptor, itf);
                                }
                            };
                        }
                    }, 0);
                    bytes = writer.toByteArray();
                }
                ZipEntry copy = new ZipEntry(entry.getName());
                copy.setTime(entry.getTime());
                out.putNextEntry(copy);
                out.write(bytes);
                out.closeEntry();
            }
        }
        if (removed[0] != 1) throw new IllegalStateException("Expected one call, found " + removed[0]);
        try (ZipFile before = new ZipFile(input.toFile()); ZipFile after = new ZipFile(output.toFile())) {
            if (before.size() != after.size()) throw new IllegalStateException("Entry count changed");
            int changed = 0;
            for (var entries = before.entries(); entries.hasMoreElements();) {
                ZipEntry e = entries.nextElement();
                try (var a = before.getInputStream(e); var b = after.getInputStream(after.getEntry(e.getName()))) {
                    if (!Arrays.equals(a.readAllBytes(), b.readAllBytes())) {
                        if (!e.getName().equals(target)) throw new IllegalStateException("Unexpected change: " + e.getName());
                        changed++;
                    }
                }
            }
            if (changed != 1) throw new IllegalStateException("Expected one changed class");
        }
        System.out.println("Verified: one registration call removed; every other JAR entry identical.");
    }
}
