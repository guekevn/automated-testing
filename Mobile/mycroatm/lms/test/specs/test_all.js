describe('Automasi Pengujian Aplikasi - Semua Tes', () => {

    it('should successfully run positive tests', async () => {
        // Menjalankan semua tes positif
        await require('./login.js'),
        await require('./cek_saldo.js')
        // await require('./transfer.js'), 
        // await require('./tarik_tunai.js'),
        // await require('./history.js')
    });
});
