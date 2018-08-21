library(shiny)
ui <- fluidPage(
  # Application title
  headerPanel("花生品质功能预测"),
  flowLayout( # object 1,
    # object 2,
    # object 3
    numericInput("含水量", "含水量  g/100g", 10),
    numericInput("脂肪含量", "脂肪含量  g/100g", 10),
    numericInput("棕榈酸", "棕榈酸  g/100g", 10),
    numericInput("油酸", "油酸  g/100g", 10),
    numericInput("不饱和脂肪酸", "不饱和脂肪酸  g/100g", 10),
    numericInput("天门冬氨酸", "天门冬氨酸 g/100g", 10),
    numericInput("亚油酸", "亚油酸 g/100g", 10),
    numericInput("粗纤维", "粗纤维  g/100g", 10),
    numericInput("苏氨酸", "苏氨酸 g/100g", 10),
    numericInput("谷氨酸", "谷氨酸 g/100g", 10),
    numericInput("异亮氨酸", "异亮氨酸 g/100g", 10),
    numericInput("亮氨酸", "亮氨酸  g/100g", 10),
    numericInput("精氨酸", "精氨酸 g/100g", 10),
    submitButton("Update View")
  ),
  mainPanel(
    h4("花生油"),
    verbatimTextOutput("huashengyou"),
    
    h4("花生酱"),
    verbatimTextOutput("huashengjiang"),
    h4("花生蛋白：凝胶性"),
    verbatimTextOutput("hsdbnj"),
    
    h4("花生蛋白：溶解性"),
    verbatimTextOutput("hsdbrj")
  )
)
server <- function(input, output) {
  beta_hsy = 1:13
  beta_hsj = 1:13
  beta_hsdbnj= 1:13
  beta_hsdbrj = 1:13
  # Generate a summary of the dataset
  output$huashengyou <- renderPrint({
    ex=sum(input$含水量*beta_hsy[1]+input$脂肪含量*beta_hsy[2]+input$棕榈酸*beta_hsy[3]+input$油酸*beta_hsy[4]+
             input$不饱和脂肪酸*beta_hsy[5]+input$天门冬氨酸*beta_hsy[6]+input$亚油酸*beta_hsy[7]+input$粗纤维*beta_hsy[8]+
             input$苏氨酸*beta_hsy[9]+input$谷氨酸*beta_hsy[10]+input$异亮氨酸*beta_hsy[11]+input$亮氨酸*beta_hsy[12]+
             input$精氨酸*beta_hsy[13])
    ex = rep(0,3)
    ex["适宜"] = 0.3
    ex["other"] = 0.1
    ex["不适宜"] = 1-ex["适宜"]-ex["other"]
    names(which.max(ex))
  })
  
  # Show the first "n" observations
  output$huashengjiang <- renderPrint({
    ex=sum(input$含水量*beta_hsj[1]+input$脂肪含量*beta_hsj[2]+input$棕榈酸*beta_hsj[3]+input$油酸*beta_hsj[4]+
             input$不饱和脂肪酸*beta_hsj[5]+input$天门冬氨酸*beta_hsj[6]+input$亚油酸*beta_hsj[7]+input$粗纤维*beta_hsj[8]+
             input$苏氨酸*beta_hsj[9]+input$谷氨酸*beta_hsj[10]+input$异亮氨酸*beta_hsj[11]+input$亮氨酸*beta_hsj[12]+
             input$精氨酸*beta_hsj[13])
    ex = rep(0,3)
    ex["适宜"] = 0.3
    ex["other"] = 0.1
    ex["不适宜"] = 1-ex["适宜"]-ex["other"]
    names(which.max(ex))
  })
  output$hsdbnj<- renderPrint({
    ex=sum(input$含水量*beta_hsdbnj[1]+input$脂肪含量*beta_hsdbnj[2]+input$棕榈酸*beta_hsdbnj[3]+input$油酸*beta_hsdbnj[4]+
             input$不饱和脂肪酸*beta_hsdbnj[5]+input$天门冬氨酸*beta_hsdbnj[6]+input$亚油酸*beta_hsdbnj[7]+input$粗纤维*beta_hsdbnj[8]+
             input$苏氨酸*beta_hsdbnj[9]+input$谷氨酸*beta_hsdbnj[10]+input$异亮氨酸*beta_hsdbnj[11]+input$亮氨酸*beta_hsdbnj[12]+
             input$精氨酸*beta_hsdbnj[13])
    ex = rep(0,3)
    ex["适宜"] = 0.3
    ex["other"] = 0.1
    ex["不适宜"] = 1-ex["适宜"]-ex["other"]
    names(which.max(ex))
  })
  output$hsdbrj<- renderPrint({
    ex=sum(input$含水量*beta_hsdbrj[1]+input$脂肪含量*beta_hsdbrj[2]+input$棕榈酸*beta_hsdbrj[3]+input$油酸*beta_hsdbrj[4]+
             input$不饱和脂肪酸*beta_hsdbrj[5]+input$天门冬氨酸*beta_hsdbrj[6]+input$亚油酸*beta_hsdbrj[7]+input$粗纤维*beta_hsdbrj[8]+
             input$苏氨酸*beta_hsdbrj[9]+input$谷氨酸*beta_hsdbrj[10]+input$异亮氨酸*beta_hsdbrj[11]+input$亮氨酸*beta_hsdbrj[12]+
             input$精氨酸*beta_hsdbrj[13])
    ex = rep(0,3)
    ex["适宜"] = 0.3
    ex["other"] = 0.1
    ex["不适宜"] = 1-ex["适宜"]-ex["other"]
    names(which.max(ex))
  })
}
shinyApp(ui = ui, server = server)
