

# TASK

Avem industriile:

	- beauty
	- fashion
	- gadgets
	- games
	- household
	- food
	- sports

Și un cuvant: ```soap```

Din care industrii face parte acest cuvant?


## Proces 

Folosind ```Wikipedia CategoryTree``` pentru fiecare industrie se scoate informația despre categoria și subcategoriile din care face parte.

- pentru fiecare industrie se descarcă pagina de pe Wikipedia (```BeautifulSoap```)

- se păstrează informația despre Categori (from the bottom of the page)

- pentru prima  categorie, care este (main category, se extrag subcategoriile (```wiki API```) și se păstrează în fișier .txt


- se extrage lista de categorii a cuvantului ```soap```

- se controlează dacă categoriile se regăsesc în fișierele .txt a industriilor 


### Resultat:

beauty -> Skin care

fashion -> Skin care

household -> Cleaning