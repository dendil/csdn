```bash
 wget -O /usr/share/vim/vim74/syntax/nginx.vim https://www.vim.org/scripts/download_script.php?src_id=19394
```
```bash
echo   'au BufRead,BufNewFile /usr/local/nginx/* set ft=nginx' >> /usr/share/vim/vim74/filetype.vim
```
