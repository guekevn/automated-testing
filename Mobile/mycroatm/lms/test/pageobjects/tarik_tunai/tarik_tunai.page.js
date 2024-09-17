const tarikTunaiActions = require('./actions')
const path = require('path')

class tarikTunaiPage {
    constructor () {
        this.screenshotDir = path.join(__dirname, '../screenshots/tarik_tunai')
    }
    async tarikTunai(nominal) {
        await tarikTunaiActions.tarikTunaiTabungan(nominal)
        await tarikTunaiActions.insertCardPage()
        await tarikTunaiActions.inputPINPage()
        await tarikTunaiActions.successTarikTunaiPage()
    }
}

module.exports = new tarikTunaiPage()