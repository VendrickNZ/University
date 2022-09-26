.class public Program
.super java/lang/Object
.method public <init>()V
aload_0
invokenonvirtual java/lang/Object/<init>()V
return
.end method
.method public static main([Ljava/lang/String;)V
.limit locals 5
.limit stack 1024
new java/util/Scanner
dup
getstatic java/lang/System.in Ljava/io/InputStream;
invokespecial java/util/Scanner.<init>(Ljava/io/InputStream;)V
astore 0
sipush 6
istore 1
sipush 3
istore 2
sipush 0
istore 3
aload 0
invokevirtual java/util/Scanner.nextInt()I
istore 4
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 4
invokestatic java/lang/String/valueOf(I)Ljava/lang/String;
invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
sipush 3
sipush 5
if_icmpeq l3
goto l2
l3:
goto l1
l2:
sipush 5
sipush 8
imul
sipush 9
idiv
istore 4
iload 1
iload 2
idiv
istore 3
l1:
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 3
invokestatic java/lang/String/valueOf(I)Ljava/lang/String;
invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 4
invokestatic java/lang/String/valueOf(I)Ljava/lang/String;
invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
return
.end method
