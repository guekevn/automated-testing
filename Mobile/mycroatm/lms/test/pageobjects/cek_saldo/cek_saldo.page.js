const path = require('path')
const cekSaldoActions = require('./actions')

class cekSaldoMenu {
    constructor(){
        this.screenshotDir = path.join(__dirname, '../screenshots/cek_saldo')
    }
    async cekSaldo (){
        await cekSaldoActions.cekSaldoTabungan()
        await cekSaldoActions.insertCardPage()
        await cekSaldoActions.inputPINPage()
        await cekSaldoActions.successPage()
    }
}

module.exports = new cekSaldoMenu()