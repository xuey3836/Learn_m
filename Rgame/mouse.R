mouse <- function() {
  # 设置画布无边
  par(mai=rep(0,4),oma=rep(0,4))

  # 初始化的点
  ps<-data.frame(x=c(0.5),y=c(0.5),col=c(2),pch=c(15))

  # x,y为鼠标坐标
  draw<-function(x=0,y=0){
    plot(0,0,xlim=c(0,1),ylim=c(0,1),type='n',xaxs="i", yaxs="i")
    abline(h=0.5,col="gray60") # 水平线
    abline(v=0.5,col="gray60") # 垂直线
    points(ps$x,ps$y,pch=ps$pch,cex=2,col=ps$col) # 实点标点
    points(x,y,pch=15,cex=2,col=colors()[ps$col]) # 鼠标坐标点
    text(0.25,0.015,label=paste(x,y,sep=",")) # 鼠标坐标
  }

  # 鼠标按键监听
  # 当鼠标按键，会增加一个实点
  # buttons,0是左键,1是滚轮,2是右键
  mouseDown <- function(buttons, x, y) {
    print(paste("down",buttons,x,y))

    # 形状设置
    shape<-15
    if(buttons==1) shape<-16
    if(buttons==2) shape<-17

    # 增加实点
    ps<<-rbind(ps,data.frame(x=c(x),y=c(y),pch=c(shape),col=round(runif(1,2,500))))
    #print(ps)
    draw(x,y)
  }

  # 鼠标移动监听
  mouseMove <- function(buttons, x, y) {
    print(paste("move",buttons,x,y))
    draw(x,y)
  }

  # 鼠标按键释放监听
  mouseup <- function(buttons, x, y) {
    print(paste("up",buttons,x,y))
    draw(x,y)
  }

  # 键盘按键监听
  keydown <- function(key) {
    if (key == "q") return(invisible(1))
  }

  # 画初始坐标
  draw()

  # 注册事件
  getGraphicsEvent(prompt="mouse",onMouseDown=mouseDown,onMouseMove=mouseMove,onMouseUp=mouseup,onKeybd=keydown)
}

# 启动程序
mouse()