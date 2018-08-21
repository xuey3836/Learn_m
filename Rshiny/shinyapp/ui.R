library(shiny)

# Define UI for miles per gallon application
shinyUI(pageWithSidebar(
  
  # Application title
  headerPanel("花生品质功能预测"),
  
  sidebarPanel(
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
    submitButton("Update View")),
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
))