[![Twitter: romy](https://img.shields.io/twitter/follow/RomySihananda)](https://twitter.com/RomySihananda)

# craw-kompas

![](https://raw.githubusercontent.com/RomySaputraSihananda/RomySaputraSihananda/main/images/GAWoFxAbkAEfUHg.jpeg)

Program ini dirancang untuk melakukan web scraping pada situs berita Kompas dengan memanfaatkan </br>parameter seperti kategori (category), tanggal, dan halaman (page). </br>Tujuan utama dari program ini adalah untuk mengumpulkan informasi berita dari Kompas sesuai </br>dengan kriteria yang diinputkan oleh pengguna.

## Requirements

- **Python >= 3.11.4**
- **pyquery >= 2.0.0**
- **pytz >= 2023.3.post1**
- **Requests >= 2.31.0**

## Installation

```sh
# Clonig Repository
git clone https://github.com/romysaputrasihananda/craw-Kompas

# Change Directory
cd craw-Kompas

# Install Requirement
pip install -r requirements.txt
```

## Example Usages

```sh
python main.py --site=News --page=2 --date=2023-12-08 --output=data
```

### Flags

| Flag     | Alias |             Description             | Example           | Default |
| :------- | :---: | :---------------------------------: | :---------------- | :-----: |
| --site   |  -s   | [category](Category.md) of the site | --site=News       |  News   |
| --page   |  -p   |       number page of the site       | --page=2          |    1    |
| --date   |  -d   |          date of the site           | --date=2023-12-08 |   now   |
| --output |  -o   |        json file output path        | --output=data     |  data   |

## Sample Output

```json
{
  "title": "Indeks Berita News Halaman 2 - 8 Desember 2023 - Kompas.com",
  "url": "https://indeks.kompas.com/?site=news&date=2023-12-08&page=2",
  "date_now": "2023-12-08T23:14:29",
  "site": "news",
  "date": "2023-12-08",
  "page": 2,
  "prev_page": 1,
  "next_page": 3,
  "data": [
    {
      "id": "eee0aa791b405408b6fe3f3c6d14fe36",
      "title": "4 Anak di Jagakarsa Dibunuh Dalam Keadaan Sadar",
      "lang": "id",
      "url": "https://megapolitan.kompas.com/read/2023/12/08/21203891/4-anak-di-jagakarsa-dibunuh-dalam-keadaan-sadar",
      "url_thumbnail": "https://asset.kompas.com/crops/qh0q7KGJQdgjzqGO5SEFFzbxYEU=/0x0:0x0/1200x800/data/photo/2023/12/07/6570bf1b45cd4.jpg",
      "create_at": "2023-12-08T21:20:38",
      "source": "Kompas.com",
      "autor": "Dzaky Nurcahyo",
      "editor": "Akhdi Martin Pratama",
      "desc": "Kasat Reskrim Polres Metro Jakarta Selatan AKBP Bintoro mengatakan, Panca Darmansyah (41) membunuh e...",
      "article": "Kasat Reskrim Polres Metro Jakarta Selatan AKBP Bintoro mengatakan, Panca Darmansyah (41) membunuh empat buah hatinya saat anak dalam kondisi sadar.\u201cYang bersangkutan melakukan pembunuhan saat anaknya dalam kondisi sadar,\u201d ujar dia di Mapolres Metro Jakarta Selatan, Jumat (8/12/2023).Bintoro menyebut, Panca membunuh semua anaknya dengan cara dibekap satu per satu.Mulanya, tersangka membekap anak bungsunya, As (1). Selang 15 menit, anak ketiga berinisial A (3) menjadi sasaran Panca.Setelah dua anaknya dipastikan tewas, pembunuhan dilanjutkan kepada anaknya yang berinisial S (4) dan VA (6).\u201cYang terakhir (dibunuh) adalah anak tertua, yang berusia 6 tahun. Jadi tersangka melakukan pembunuhan dengan jarak 15 menit,\u201d tutur dia.Adapun, waktu pembunuhan dilakukan pada Minggu, 3 Desember 2023, di kontrakan tersangka. Panca membunuh empat anak kandungnya dalam rentang waktu pukul 13.00-14.00 WIB.Diberitakan sebelumnya, warga Gang Haji Roman, RT 04 RW 03, Jagakarsa, Jakarta Selatan, Rabu sore, terganggu oleh bau busuk yang menyengat.Setelah ditelusuri, bau berasal dari sebuah rumah kontrakan yang dihuni pasangan suami istri bernama Panca Darmansyah (41) dan D beserta anak-anaknya.Di dalam rumah, warga bersama polisi menemukan keempat anak Panca dan D dalam keadaan tewas di salah satu kamar. Keempatnya berinisial VA (6), S (4), A (3), dan As (1).Tidak hanya itu, Panca ditemukan terlentang lemas di kamar mandi dengan lengan terluka. Sebilah pisau yang diduga digunakan untuk menyayat tubuhnya juga ditemukan di dekatnya.Sejauh ini, penyidik menduga, Panca tega menghabisi nyawa anak-anaknya sendiri sebelum hendak bunuh diri.Adapun, istri Panca berinisial D diketahui sedang dirawat di salah satu rumah sakit di RSUD Pasar Minggu. D dirawat intensif akibat kekerasan dalam rumah tangga yang dilakukan Panca pada Sabtu (2/12/2023).",
      "tags": [
        "kasus pembunuhan 4 bocah di Jagakarsa",
        "kasus dugaan pembunuhan empat anak di jagakarsa",
        "Ayah 4 Anak yang Tewas di Jagakarsa Jadi Tersangka",
        "Panca Darmansyah Ditetapkan Tersangka"
      ]
    }
    // ... more data
  ]
}
```

## License

This project is licensed under the [MIT License](LICENSE).
