
# 字母工具
letter<-function(){
  
  # 画图函数
  draw<-function(label='',x=0,y=0){
    plot(x,y,type='n')
    text(x,y,label=label,cex=5)
  }
  
  # 键盘事件
  keydown<-function(K){
    if (K == "ctrl-C") return(invisible(1))
    print(K)
    draw(K)
  }
  
  # 画图
  draw()
  
  # 注册键盘事件，启动监听
  getGraphicsEvent(prompt="Letter Tool",onKeybd = keydown)
}

#启动程序
letter()