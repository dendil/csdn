

	if [ "${num}" == "1" ]; then
	    install_panel_and_node 1   install_panel_and_node 1
	else
	    stty erase '^H' && read -p " 请输入数字 [1-3]:" numstty erase '^H' && read -p " 请输入数字 [1-3]:" num
			case "$num" incase "$num" in
由于终端默认ctrl + backspace 为删除 操作很不方便，这样设置后 直接backspace就能删除了。

