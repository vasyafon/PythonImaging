set nocompatible
set ruler
set showcmd
"set nu
set foldmethod=indent
set incsearch
set autoindent
set smartindent

set spell spelllang=ru_yo,en_us
set nospell
set expandtab
set shiftwidth=4
set softtabstop=4
set tabstop=4
set novisualbell "Не мигать

set keymap=russian-jcukenwin
set iminsert=0
set imsearch=0

if !exists(":DiffOrig")
    command DiffOrig vert new | set bt=nofile | r # | 0d_ | diffthis
          \ | wincmd p | diffthis
endif

imap <INSERT> <Esc>
nmap <DELETE> <INSERT> <DELETE>
nmap <F8> <ESC>:set invnu<cr>
imap <F8> <ESC>:set invnu<cr><INSERT>
let python_highlight_all = 1

function InsertTabWrapper()
     let col = col('.') - 1
     if !col || getline('.')[col - 1] !~ '\k'
         return "\<tab>"
     else
         return "\<c-p>"
     endif
endfunction
"imap <tab> <c-r>=InsertTabWrapper()<cr>
"vnoremap < vnoremap > >gv
imap <tab> <ESC>>><INSERT>
imap <s-tab> <ESC><<<INSERT>
nmap <tab> <ESC>>>
nmap <s-tab> <ESC><<

vmap <tab> >zogv
vmap <s-tab> <gv

imap <F12> <ESC>:set autoindent smartindent<cr><INSERT>
nmap <F12> <ESC>:set autoindent smartindent<cr><INSERT>
imap <F11> <ESC>:set noautoindent nosmartindent<cr><INSERT>
nmap <F11> <ESC>:set noautoindent nosmartindent<cr><INSERT>

imap <C-t> <ESC>:tabnew <cr>
nmap <C-t> :tabnew <cr>
imap <C-w> <ESC>:tabclose <cr>
nmap <C-w> :tabclose <cr>

nmap p P

imap <C-P> printf("\n");<LEFT><LEFT><LEFT><LEFT><LEFT>
imap <C-O> /** <TAB>\brief <TAB><TAB>\english \endenglish <cr><TAB><TAB><TAB><TAB><TAB>\russian \endrussian <cr><BACKSPACE><BACKSPACE><BACKSPACE>\details <TAB>\english \endenglish <cr><TAB><TAB><TAB>\russian \endrussian<cr><BACKSPACE><BACKSPACE><BACKSPACE><BACKSPACE><BACKSPACE>*/

"Visual mode copy-paste
imap <M-Down> <ESC>V
imap <M-Up> <ESC>V
nmap <M-Down> <ESC>V
nmap <M-Up> <ESC>V
vmap <M-Down> j
vmap <M-Up> k
vmap <Down> <ESC> i
vmap <Up> <ESC>   i
imap <M-Left> <ESC>vh
imap <M-Right> <ESC>vl
nmap <M-Left> <ESC>vh
nmap <M-Right> <ESC>vl
vmap <M-Left> h
vmap <M-Right> l
vmap <Left> <ESC> i
vmap <Right> <ESC> i
vmap <C-c> y
imap <C-v> <ESC>P<INSERT>
nmap <C-v> P<INSERT>


imap <F2> <ESC>:w<cr><INSERT>
nmap <F2> <ESC>:w<cr>
imap <F10> <ESC>:wq<cr><INSERT>
nmap <F10> <ESC>:wq<cr><INSERT>
imap <C-F10> <ESC>:q!<cr><INSERT>
nmap <C-F10> <ESC>:q!<cr><INSERT>
imap <C-Z> <ESC>u<cr><INSERT>
vmap <C-Z> <ESC>u<cr>
imap <C-B> <ESC>:red<cr><INSERT>
nmap <C-Z> <ESC>u<cr>
nmap <C-B> <ESC>:red<cr>

imap <F5> <ESC>zc<cr><INSERT>
nmap <F5> <ESC>zc<cr>
imap <C-F5> <ESC>zM<cr><INSERT>
nmap <C-F5> <ESC>zM<cr>
imap <F6> <ESC>zo<cr><INSERT>
nmap <F6> <ESC>zo<cr>
imap <C-F6> <ESC>zR<cr><INSERT>
nmap <C-F6> <ESC>zR<cr>

imap <C-V> "+gPi

"nmap <F10101010101010101010et mouse=a<cr><INSERT>
"imap <F10> <ESC>:set mouse=a<cr><INSERT>
"nmap <F9>  <ESC>:set mouse=""<cr><INSERT>
"imap <F9>  <ESC>:set mouse=""<cr><INSERT>

nmap <F7>  <ESC>:%s/from/to/gc
imap <F7>  <ESC>:%s/from/to/gc

set complete=""
set complete+=.
set complete+=k
set complete+=b
set complete+=t
autocmd FileType make set noexpandtab
autocmd FileType python set omnifunc=pythoncomplete#Complete
imap <c-r>  InsertTabWrapper()"Показываем все полезные опции автокомплита сразу
