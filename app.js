const express = require('express')

const app = express()
app.use(express.json())
const PORT = 3300


let command=''

app.get('/page',(req,res)=>{
  res.sendFile(__dirname+'/index.html')
})

app.get('/',(req,res)=>{
  res.send(command)
})

app.post('/',(req,res)=>{
  console.log(req.body.ex)
  command=req.body.ex
  res.send({'ok':'ok'})
})

app.listen(PORT)