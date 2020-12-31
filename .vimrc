set nocompatible
filetype off
set number

" Intitialize Vundle plugin manager
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" Vundle
Plugin 'VundleVim/Vundle.vim'

" LightLine
Plugin 'itchyny/lightline.vim'

" End of plugin list
call vundle#end()
filetype plugin indent on

" Lightline theme
set laststatus=2
let g:lightline = {'colorscheme': 'darcula',}

