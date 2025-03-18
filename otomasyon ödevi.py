print(" DERS OTOMASYON SİSTEMİNE HOŞGELDİNİZ")
kullanıcı_adı = "123"
sifre = "123"
g_k = str(input("KULLANICI ADINIZI GİRİNİZ="))
g_s = str(input("KULLANICI ŞİFRENİZİ GİRİNİZ="))
if (g_k == "123"):
     if (g_s == "123"):
          print("GİRİŞ BAŞARILI")
          ö_g = int(input("İŞLEM YAPMAK İSTEĞİNİZ ÖĞRENCİ NUMARASINI GİRİNİZ="))
          if ö_g >=15 and ö_g <=18:
               if ö_g == 15:
                    print("ÖĞRENCİ=AHMET YALÇIN \nÖĞRENCİ NO=15\n 1.SINIF")
               if ö_g == 16:
                    print("ÖĞRENCİ=MEHMET KAYA \nÖĞRENCİ NO = 16\n 1.SINIF")
               if ö_g == 17:
                    print("ÖĞRENCİ=HÜSEYİN YILDIZ \nÖĞRENCİ NO = 17\n 1.SINIF")
               if ö_g == 18:
                    print("ÖĞRENCİ=HAVZETE TEPE \nÖĞRENCİ NO = 18\n 1.SINIF")

               mat_vize = int(input("MATEMATİK VİZE NOTUNU GİRİNİZ="))
               mat_final = int(input("MATEMATİK FİNAL NOTUNU GİRİNİZ="))
               mat_ort = ((mat_vize * 30) / 100) + ((mat_final * 70) / 100)

               if mat_ort >= 90:
                    print(mat_ort, "AA ")
               if mat_ort >= 80 and mat_ort < 90:
                    print(mat_ort, "BA")
               if mat_ort >= 75 and mat_ort < 80:
                    print(mat_ort, "BB")
               if mat_ort >= 70 and mat_ort < 75:
                    print(mat_ort, "CB")
               if mat_ort >= 60 and mat_ort < 70:
                    print(mat_ort, "CC")
               if mat_ort >= 50 and mat_ort < 60:
                    print(mat_ort, "DC (KOŞULLU BAŞARILI)")
               if mat_ort < 50:
                    print(mat_ort, "DD  (BAŞARISIZ) ")

               türkdili_vize = int(input("TÜRK DİLİ VİZE NOTUNU GİRİNİZ="))
               türkdili_final = int(input("TÜRK DİLİ FİNAL NOTUNU GİRİNİZ="))
               türkdili_ort = ((türkdili_vize * 30) / 100) + ((türkdili_final * 70) / 100)

               if türkdili_ort >= 90:
                    print(türkdili_ort, "AA ")
               if türkdili_ort >= 80 and türkdili_ort < 90:
                    print(türkdili_ort, "BA")
               if türkdili_ort >= 75 and türkdili_ort < 80:
                    print(türkdili_ort, "BB")
               if türkdili_ort >= 70 and türkdili_ort < 75:
                    print(türkdili_ort, "CB")
               if türkdili_ort >= 60 and türkdili_ort < 70:
                    print(türkdili_ort, "CC")
               if türkdili_ort >= 50 and türkdili_ort < 60:
                    print(türkdili_ort, "DC (KOŞULLU BAŞARILI)")
               if türkdili_ort < 50:
                    print(türkdili_ort, "DD  (BAŞARISIZ) ")

               algoritma_vize = int(input("ALGORİTMA VİZE NOTUNU GİRİNİZ="))
               algoritma_final = int(input("ALGORİTMA FİNAL NOTUNU GİRİNİZ="))
               algoritma_ort = ((algoritma_vize * 30) / 100) + ((algoritma_final * 70) / 100)

               if algoritma_ort >= 90:
                    print(algoritma_ort, "AA ")
               if algoritma_ort >= 80 and algoritma_ort < 90:
                    print(algoritma_ort, "BA")
               if algoritma_ort >= 75 and algoritma_ort < 80:
                    print(algoritma_ort, "BB")
               if algoritma_ort >= 70 and algoritma_ort < 75:
                    print(algoritma_ort, "CB")
               if algoritma_ort >= 60 and algoritma_ort < 70:
                    print(algoritma_ort, "CC")
               if algoritma_ort >= 50 and algoritma_ort < 60:
                    print(algoritma_ort, "DC (KOŞULLU BAŞARILI)")
               if algoritma_ort < 50:
                    print(algoritma_ort, "DD  (BAŞARISIZ) ")

               istatistik_vize = int(input("İSTATİSTİK VİZE NOTUNU GİRİNİZ="))
               istatistik_final = int(input("İSTATİSTİK FİNAL NOTUNU GİRİNİZ="))
               istatistik_ort = ((istatistik_vize * 30) / 100) + ((istatistik_final * 70) / 100)

               if istatistik_ort >= 90:
                    print(istatistik_ort, "AA ")
               if istatistik_ort >= 80 and istatistik_ort < 90:
                    print(istatistik_ort, "BA")
               if istatistik_ort >= 75 and istatistik_ort < 80:
                    print(istatistik_ort, "BB")
               if istatistik_ort >= 70 and istatistik_ort < 75:
                    print(istatistik_ort, "CB")
               if istatistik_ort >= 60 and istatistik_ort < 70:
                    print(istatistik_ort, "CC")
               if istatistik_ort >= 50 and istatistik_ort < 60:
                    print(istatistik_ort, "DC (KOŞULLU BAŞARILI)")
               if istatistik_ort < 50:
                    print(istatistik_ort, "DD  (BAŞARISIZ) ")

               excel_vize = int(input("EXCEL VİZE NOTUNU GİRİNİZ="))
               excel_final = int(input("EXCEL FİNAL NOTUNU GİRİNİZ="))
               excel_ort = ((excel_vize * 30) / 100) + ((excel_final * 70) / 100)
               genel_ortalama = (((5 * (mat_ort)) + (2 * (türkdili_ort)) + (3 * (algoritma_ort)) + (
                       2 * (istatistik_ort)) + (excel_ort)) / (13 * 25))
               if excel_ort >= 90:
                    print(excel_ort, "AA ")
               if excel_ort >= 80 and excel_ort < 90:
                    print(excel_ort, "BA")
               if excel_ort >= 75 and excel_ort < 80:
                    print(excel_ort, "BB")
               if excel_ort >= 70 and excel_ort < 75:
                    print(excel_ort, "CB")
               if excel_ort >= 60 and excel_ort < 70:
                    print(excel_ort, "CC")
               if excel_ort >= 50 and excel_ort < 60:
                    print(excel_ort, "DC (KOŞULLU BAŞARILI)")
               if excel_ort < 50:
                    print(excel_ort, "DD  (BAŞARISIZ) ")
               if excel_ort < 0:
                    print("")
               else:
                    print()
                    print("GENEL ORTALAMANIZ =", genel_ortalama)

                    if genel_ortalama < 2:
                         print("SINIF TEKRARI")
                    else:
                         print("GEÇTİNİZ")

          else:
               print("ÖĞRENCİ NUMARASI YANLIŞ")



     else:
          print("GİRİŞ BAŞARISIZ")
else:
     print("KULLANICI ADI,ŞİFRE YANLIŞ")