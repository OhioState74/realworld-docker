const express=require('express')
const app =express();

app.get('/test',(req,res) => {
   res.send('our api server is work')
});
app.listen(3000,() =>{
    console.log('started api service')
});

