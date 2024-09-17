const fs = require('fs')
const path = require('path')

function createScreenshotDir(dirPath){
    if (!fs.existsSync(dirPath)) { 
        fs.mkdirSync(dirPath, { recursive: true })
        console.log(`Directory created : ${dirPath}`)
    }
    return dirPath
}

async function takeScreenshot(dirPath, fileName){
    createScreenshotDir(dirPath)
    await global.browser.saveScreenshot(path.join(dirPath, `${fileName}.png`))
}

module.exports = {createScreenshotDir, takeScreenshot}