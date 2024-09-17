const transferActions = require('./actions')
const path = require('path')

class transferPage {
    constructor () {
        this.screenshotDir = path.join(__dirname, '../screenshots/transfer')
    }

    async transfer (rekening, nominal) {
        await transferActions.selectTransferBRI.click()
        await transferActions.inputTransferDetails(rekening, nominal)
        await transferActions.waitForInsertCardPage()
        await transferActions.waitForInsertPINPage()
        await transferActions.waitForSuccessPage()
        await transferActions.successTransferPage()
    }
}

module.exports = new transferPage()