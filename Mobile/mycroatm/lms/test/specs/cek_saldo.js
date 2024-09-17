const cekSaldoMenu = require('../pageobjects/cek_saldo/cek_saldo.page')

describe('Cek Saldo Aplikasi LMS', () => {
    it('Cek Saldo berhasil', async () => {
        await cekSaldoMenu.cekSaldo()
    })
})