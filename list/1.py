import os
fn = os.listdir('/home/ssh-ubuntu/blog/hexo/themes/Sakura/source/music/')
with open ('music.md','a') as f :
    for i in range(0,68):
        n = fn[i] 
        f.write('{% aplayer "'+n+' "" '+'""https://juanhu.tk/music/'+n+'" "https://juanhu.tk/images/1.jpg" %}')
        f.write('\n')
