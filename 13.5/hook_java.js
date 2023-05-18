Java.perform(() => {
  let MainActivity = Java.use('com.germey.appbasic1.MainActivity')
  console.log('start hook')
  MainActivity.getMessage.implementation = () => {
    send('Start Hook!')
    return '6'
  }
})