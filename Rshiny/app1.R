library(shiny)
ui <- fluidPage(
  # Application title
  headerPanel("花生品质功能预测"),
  flowLayout( # object 1,
    # object 2,
    # object 3
    numericInput("含水量", "含水量  g/100g", 10),
    numericInput("含油量", "含油量  g/100g", 10),
    numericInput("酸价","酸价", 1 ),
    # numericInput("含油量", "含油量  g/100g", value = 10),
    numericInput("蛋白质含量","蛋白质含量 g/100g", value=10),
    numericInput("棕榈酸", "棕榈酸  g/100g", 10),
    numericInput("蛋氨酸","蛋氨酸 g/100g", value = 10),
    numericInput("精氨酸", "精氨酸 g/100g", value = 10),
    numericInput("油酸", "油酸 g/100g", 10),
    numericInput("OL","OL",value= 10),
    numericInput("不饱和脂肪酸", "不饱和脂肪酸  g/100g", 10),
    numericInput("天门冬氨酸", "天门冬氨酸 g/100g", value = 10),
    numericInput("亚油酸", "亚油酸 g/100g", 10),
    numericInput("粗纤维", "粗纤维  g/100g", 10),
    numericInput("苏氨酸", "苏氨酸 g/100g", 10),
    numericInput("谷氨酸", "谷氨酸 g/100g", 10),
    numericInput("异亮氨酸", "异亮氨酸 g/100g", 10),
    numericInput("亮氨酸", "亮氨酸  g/100g", 10),
    numericInput("花生酸","花生酸 g/100g", 10),
    submitButton("Update View")
  ),
  mainPanel(
    h4(strong("花生油")),
    verbatimTextOutput("huashengyou"),
    
    h4(strong("花生酱")),
    verbatimTextOutput("huashengjiang"),
    h4(strong("花生蛋白：凝胶性")),
    verbatimTextOutput("hsdbnj"),
    
    h4(strong("花生蛋白：溶解性")),
    verbatimTextOutput("hsdbrj")
  )
)
server <- function(input, output) {
  
  # Show the first "n" observations
  output$huashengyou= renderPrint({
    u1 = 13.725 - 0.417*input$棕榈酸^2 + 0.00167*input$亚油酸^2- 7.059*input$花生酸^2-
      0.831*input$亚油酸/input$棕榈酸- 0.218*input$亚油酸/input$花生酸+1.994/input$酸价-
      25.588/input$油酸-0.017*input$含水量^2- 0.0031*input$含油量- 0.0576*input$OL^2+0.072*input$油酸+
      0.189*input$不饱和脂肪酸+2.006*input$含水量*input$酸价- 0.562*input$酸价*input$油酸-
      0.143*input$酸价*input$OL
    u2 = 20.849 - 0.417*input$棕榈酸^2 + 0.00167*input$亚油酸^2- 7.059*input$花生酸^2-
      0.831*input$亚油酸/input$棕榈酸- 0.218*input$亚油酸/input$花生酸+1.994/input$酸价-
      25.588/input$油酸-0.017*input$含水量^2- 0.0031*input$含油量- 0.0576*input$OL^2+0.072*input$油酸+
      0.189*input$不饱和脂肪酸+2.006*input$含水量*input$酸价- 0.562*input$酸价*input$油酸-
      0.143*input$酸价*input$OL
    # u1 = 3
    # u2 = 2
    v1 = exp(u1)
    v2 = exp(u2)
    p = rep(0,3)
    p["不适宜"] = v1/(1+v1)
    p["基本适宜"] = v2/(1+v2) - v1/(1+v1)
    p["适宜"] = 1- p["不适宜"]-p["基本适宜"]
    return(names(which.max(p)))
    })
  output$huashengjiang <- renderPrint({
    u1 = -135.3133-121.3634*input$蛋氨酸^2-2.3718/(input$蛋氨酸^2)+8.5160/(input$OL^2)+
      13.6826*log(input$含油量)+48.4477*log(input$蛋白质含量)+15.6472*log(input$天门冬氨酸)-15.7329*log(input$油酸)-
      2.0589*input$精氨酸^2
    u2 = -128.5687-121.3634*input$蛋氨酸^2-2.3718/(input$蛋氨酸^2)+8.5160/(input$OL^2)+
      13.6826*log(input$含油量)+48.4477*log(input$蛋白质含量)+15.6472*log(input$天门冬氨酸)-15.7329*log(input$油酸)-
      2.0589*input$精氨酸^2
    v1 = exp(u1)
    v2 = exp(u2)
    p = rep(0,3)
    p["不适宜"] = v1/(1+v1)
    p["基本适宜"] = v2/(1+v2) - v1/(1+v1)
    p["适宜"] = 1- p["不适宜"]-p["基本适宜"]
    print(names(which.max(p)))
  })
  output$hsdbnj<- renderPrint({
    u =  43.3235- 5.8742/(input$粗纤维^2)+2.5718*input$天门冬氨酸*input$异亮氨酸-14.2342*input$异亮氨酸/input$天门冬氨酸-
      11.0155*input$天门冬氨酸/input$亮氨酸+0.4072*input$谷氨酸/input$苏氨酸-
      30.9734*input$苏氨酸/input$亮氨酸-47.9375*input$异亮氨酸/input$精氨酸
    p1 = exp(u)/(1+exp(u))
    p2 = 1/(1+exp(u))
    p = p2- p1 
    if ( p >0.33){
      return("适宜")
    }else if( -0.33 < p | p < 0.33){
      return("基本适宜")
    }else{
      return("不适宜")
    }})
  output$hsdbrj<- renderPrint({
     u = -100.2 - 0.0370* input$粗纤维^2- 1.5610*input$精氨酸+0.004978/(input$苏氨酸^2)-
       309.5/(input$谷氨酸^2)+7.0861*input$苏氨酸/(input$粗纤维)-2.9472*input$天门冬氨酸*input$亮氨酸+
       182.34*input$苏氨酸/input$亮氨酸+33.648*input$亮氨酸/input$苏氨酸-10.903*input$谷氨酸/input$精氨酸
     p1 = exp(u)/(1+exp(u))
     p2 = 1/(1+exp(u))
     p = p2- p1 
     if ( p >0.33){
       return("适宜")
     }else if( -0.33 < p | p < 0.33){
       return("基本适宜")
     }else{
       return("不适宜")
     }})
}

shinyApp(ui = ui, server = server)
