const transferMenu = require('../pageobjects/transfer/transfer.page')

describe ('Transfer Aplikasi LMS', () => {
    it('Transfer berhasil', async () => {
        await transferMenu.transfer('145201007728500', '10000')
    })
})