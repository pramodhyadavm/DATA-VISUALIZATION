

from google.colab import files

df = files.upload()
     
Upload widget is only available when the cell has been executed in the current browser session. Please rerun this cell to enable.
Saving BL-Flickr-Images-Book.csv to BL-Flickr-Images-Book.csv

import pandas as pd
data = pd.read_csv('./BL-Flickr-Images-Book.csv')
data.head()
     
Identifier	Edition Statement	Place of Publication	Date of Publication	Publisher	Title	Author	Contributors	Corporate Author	Corporate Contributors	Former owner	Engraver	Issuance type	Flickr URL	Shelfmarks
0	206	NaN	London	1879 [1878]	S. Tinsley & Co.	Walter Forbes. [A novel.] By A. A	A. A.	FORBES, Walter.	NaN	NaN	NaN	NaN	monographic	http://www.flickr.com/photos/britishlibrary/ta...	British Library HMNTS 12641.b.30.
1	216	NaN	London; Virtue & Yorston	1868	Virtue & Co.	All for Greed. [A novel. The dedication signed...	A., A. A.	BLAZE DE BURY, Marie Pauline Rose - Baroness	NaN	NaN	NaN	NaN	monographic	http://www.flickr.com/photos/britishlibrary/ta...	British Library HMNTS 12626.cc.2.
2	218	NaN	London	1869	Bradbury, Evans & Co.	Love the Avenger. By the author of “All for Gr...	A., A. A.	BLAZE DE BURY, Marie Pauline Rose - Baroness	NaN	NaN	NaN	NaN	monographic	http://www.flickr.com/photos/britishlibrary/ta...	British Library HMNTS 12625.dd.1.
3	472	NaN	London	1851	James Darling	Welsh Sketches, chiefly ecclesiastical, to the...	A., E. S.	Appleyard, Ernest Silvanus.	NaN	NaN	NaN	NaN	monographic	http://www.flickr.com/photos/britishlibrary/ta...	British Library HMNTS 10369.bbb.15.
4	480	A new edition, revised, etc.	London	1857	Wertheim & Macintosh	[The World in which I live, and my place in it...	A., E. S.	BROOME, John Henry.	NaN	NaN	NaN	NaN	monographic	http://www.flickr.com/photos/britishlibrary/ta...	British Library HMNTS 9007.d.28.

to_drop = ['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner', 'Engraver', 'Contributors', 'Issuance type', 'Shelfmarks']
data.drop(to_drop, inplace = True, axis = 1)
data.head()
     
Identifier	Place of Publication	Date of Publication	Publisher	Title	Author	Flickr URL
0	206	London	1879 [1878]	S. Tinsley & Co.	Walter Forbes. [A novel.] By A. A	A. A.	http://www.flickr.com/photos/britishlibrary/ta...
1	216	London; Virtue & Yorston	1868	Virtue & Co.	All for Greed. [A novel. The dedication signed...	A., A. A.	http://www.flickr.com/photos/britishlibrary/ta...
2	218	London	1869	Bradbury, Evans & Co.	Love the Avenger. By the author of “All for Gr...	A., A. A.	http://www.flickr.com/photos/britishlibrary/ta...
3	472	London	1851	James Darling	Welsh Sketches, chiefly ecclesiastical, to the...	A., E. S.	http://www.flickr.com/photos/britishlibrary/ta...
4	480	London	1857	Wertheim & Macintosh	[The World in which I live, and my place in it...	A., E. S.	http://www.flickr.com/photos/britishlibrary/ta...

data.set_index('Identifier',  inplace=True)
data.head()
     
Place of Publication	Date of Publication	Publisher	Title	Author	Flickr URL
Identifier						
206	London	1879 [1878]	S. Tinsley & Co.	Walter Forbes. [A novel.] By A. A	A. A.	http://www.flickr.com/photos/britishlibrary/ta...
216	London; Virtue & Yorston	1868	Virtue & Co.	All for Greed. [A novel. The dedication signed...	A., A. A.	http://www.flickr.com/photos/britishlibrary/ta...
218	London	1869	Bradbury, Evans & Co.	Love the Avenger. By the author of “All for Gr...	A., A. A.	http://www.flickr.com/photos/britishlibrary/ta...
472	London	1851	James Darling	Welsh Sketches, chiefly ecclesiastical, to the...	A., E. S.	http://www.flickr.com/photos/britishlibrary/ta...
480	London	1857	Wertheim & Macintosh	[The World in which I live, and my place in it...	A., E. S.	http://www.flickr.com/photos/britishlibrary/ta...

data['Date of Publication'].head(25)
     
Identifier
206            1879 [1878]
216                   1868
218                   1869
472                   1851
480                   1857
481                   1875
519                   1872
667                    NaN
874                   1676
1143                  1679
1280                  1802
1808                  1859
1905                  1888
1929           1839, 38-54
2836                  1897
2854                  1865
2956               1860-63
2957                  1873
3017                  1866
3131                  1899
4598                  1814
4884                  1820
4976                  1800
5382    1847, 48 [1846-48]
5385               [1897?]
Name: Date of Publication, dtype: object

import numpy as np

unwanted_characters = ['[', ',', '-']

def clean_dates(item):
    dop= str(item.loc['Date of Publication'])

    if dop == 'nan' or dop[0] == '[':
        return np.NaN

    for character in unwanted_characters:
        if character in dop:
            character_index = dop.find(character)
            dop = dop[:character_index]

    return dop

data['Date of Publication'] = data.apply(clean_dates, axis = 1)
print(data['Date of Publication'])
     
Identifier
206        1879 
216         1868
218         1869
472         1851
480         1857
           ...  
4158088     1838
4158128     1831
4159563      NaN
4159587     1834
4160339     1834
Name: Date of Publication, Length: 8287, dtype: object

print(data['Author'])
     
Identifier
206                                                    A. A.
216                                                A., A. A.
218                                                A., A. A.
472                                                A., E. S.
480                                                A., E. S.
                                 ...                        
4158088                   GIDDY, afterwards GILBERT, Davies.
4158128                           GLOVER, Stephen - of Derby
4159563    LYSONS, Daniel - M.A., F.R.S., and LYSONS (Sam...
4159587                                Mackenzie, E. (Eneas)
4160339                                                  NaN
Name: Author, Length: 8287, dtype: object

def clean_author_names(author):

    author = str(author)

    if author == 'nan':
        return 'NaN'

    author = author.split(',')

    if len(author) == 1:
        name = filter(lambda x: x.isalpha(), author[0])
        return reduce(lambda x, y: x + y, name)

    last_name, first_name = author[0], author[1]


    first_name = first_name[:first_name.find('-')] if '-' in first_name else first_name

    if first_name.endswith(('.', '.|')):
        parts = first_name.split('.')

        if len(parts) > 1:
            first_occurence = first_name.find('.')
            final_occurence = first_name.find('.', first_occurence + 1)
            first_name = first_name[:final_occurence]
        else:
            first_name = first_name[:first_name.find('.')]

    last_name = last_name.capitalize()

    return f'{first_name} {last_name}'

data['Author'] = data.apply(clean_author_names, axis=1)

     

data
     
Place of Publication	Date of Publication	Publisher	Title	Author	Flickr URL
Identifier						
206	London	1879	S. Tinsley & Co.	Walter Forbes. [A novel.] By A. A	dtype: object Place of publication ...	http://www.flickr.com/photos/britishlibrary/ta...
216	London; Virtue & Yorston	1868	Virtue & Co.	All for Greed. [A novel. The dedication signed...	A. A.\nFlickr URL http://www.fli...	http://www.flickr.com/photos/britishlibrary/ta...
218	London	1869	Bradbury, Evans & Co.	Love the Avenger. By the author of “All for Gr...	Evans & Co.\nTitle Love the...	http://www.flickr.com/photos/britishlibrary/ta...
472	London	1851	James Darling	Welsh Sketches, chiefly ecclesiastical, to the...	chiefly ecclesiastical Place of publication ...	http://www.flickr.com/photos/britishlibrary/ta...
480	London	1857	Wertheim & Macintosh	[The World in which I live, and my place in it...	and my place in it. Place of publication ...	http://www.flickr.com/photos/britishlibrary/ta...
...	...	...	...	...	...	...
4158088	London	1838	NaN	The Parochial History of Cornwall, founded on,...	founded on Place of publication ...	http://www.flickr.com/photos/britishlibrary/ta...
4158128	Derby	1831	M. Mozley & Son	The History and Gazetteer of the County of Der...	Stephen Place of publication ...	http://www.flickr.com/photos/britishlibrary/ta...
4159563	London	NaN	T. Cadell and W. Davies	Magna Britannia; being a concise topographical...	Daniel Place of publication ...	http://www.flickr.com/photos/britishlibrary/ta...
4159587	Newcastle upon Tyne	1834	Mackenzie & Dent	An historical, topographical and descriptive v...	topographical and descriptive v...\nAuthor ...	http://www.flickr.com/photos/britishlibrary/ta...
4160339	London	1834	NaN	Collectanea Topographica et Genealogica. [Firs...	dtype: object Place of publication ...	http://www.flickr.com/photos/britishlibrary/ta...
8287 rows × 6 columns



     
