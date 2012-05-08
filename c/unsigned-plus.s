	.file	"unsigned-plus.c"
	.section	.rodata
.LC0:
	.string	"%d %d\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5

	andl	$-16, %esp
	subl	$32, %esp
# 分别变量赋值0x7fffffff
	movl	$2147483647, 24(%esp) # unsigned int var_ui
	movl	$2147483647, 28(%esp) # int var_i
# 分别做加法，加1
	addl	$1, 24(%esp)    # unsigned int var_ui
	addl	$1, 28(%esp)    # int var_i
# unsigned int var_ui > 0x7fffffff 类型比较
	movl	24(%esp), %eax
	movl	%eax, %edx      # 这句估计是编译产生的废品，我直接将24(%esp)放入edx也能正确执行
	shrl	$31, %edx       # edx中数字右移31位，结果1放在edx中
# 注意，这里没有对int做任何处理

# 输出
	movl	$.LC0, %eax     # eax存储格式字符串地址
	movl	%edx, 8(%esp)   # var_ui > 0x7fffffff 比较结果存入栈
	movl	$0, 4(%esp)     # int结果入栈，这里的0是编译器直接求值的，残暴啊！！！
	movl	%eax, (%esp)    # 格式字符串地址入栈
	call	printf          # 函数调用，做输出动作
                            # 关于printf调用，可参考http://ouonline.net/att-asm-2-1
# 退出程序
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 4.6.3-1ubuntu5) 4.6.3"
	.section	.note.GNU-stack,"",@progbits
