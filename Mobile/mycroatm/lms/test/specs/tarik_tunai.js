const tarikTunaiPage = require('../pageobjects/tarik_tunai/tarik_tunai.page')

describe ('Tarik tunai aplikasi LMS', () => {
    it('Tarik tunai berhasil', async () => {
        await tarikTunaiPage.tarikTunai('10000')
    })
})