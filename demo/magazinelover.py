import pandas as pd

class MagazineLover:
    def __init__(self, name, email, fav_genre, num_magazines=0, magazine_list=pd.DataFrame({'magazine_name': [], 'magazine_rating': []})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_magazines = num_magazines
        self.magazine_list = magazine_list

    def add_magazine(self, magazine_name, rating):
        if magazine_name in self.magazine_list['magazine_name'].values:
            print(f"The magazine '{magazine_name}' already exists in the magazine list.")
        else:
            new_magazine = pd.DataFrame({
                'magazine_name': [magazine_name], 
                'magazine_rating': [rating]
            })
            self.magazine_list = pd.concat([self.magazine_list, new_magazine], ignore_index=True)
            print(f"Magazine '{magazine_name}' added successfully.")
            
    def has_read(self, magazine_name):
        return magazine_name in self.magazine_list['magazine_name'].values

    def fav_magazines(self):
        return self.magazine_list[self.magazine_list['magazine_rating'] > 3]

if __name__ == '__main__':
    
    test_object = MagazineLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_magazine("War of the Worlds", 4)
    # And so forth
    
    
    
    