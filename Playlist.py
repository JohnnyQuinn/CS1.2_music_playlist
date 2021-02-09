from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    new_song = Song(title)

    if self.__first_song == None:
      self.__first_song = new_song
    else:
      current_song = self.__first_song

      while current_song.get_next_song() != None:
        current_song = current_song.get_next_song()
      
      current_song.set_next_song(new_song)




  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    current_song = self.__first_song
    index = 0
    song_found = False

    while current_song != None:
      index += 1
      if current_song.get_title() == title:
        song_found = True
        break
      else:
        current_song = current_song.get_next_song()
    
    if song_found is True:
      return index
    else:
      return -1 


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    current_song = self.__first_song

    while current_song != None:
      
      if current_song.get_title() == title:
        while current_song.get_next_song() != None:
          current_song.set_title(current_song.get_next_song().get_title())
          current_song = current_song.get_next_song()
        else:
          current_song.set_title(None)
        # else: 
        #   current_song.set_title(None)

        # while current_song.get_next_song() != None:
        #   current_song.set_title(current_song.get_next_song().get_title())
        #   current_song = current_song.get_next_song()


        # if current_song.get_next_song() != None: 
        #   current_song.set_title(current_song.get_next_song().get_title())
        #   current_song.set_next_song(current_song.get_next_song)
        # else:
        #   current_song = None

        break
      else:
        current_song = current_song.get_next_song()



  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    current_song = self.__first_song
    counter = 0

    while current_song != None:
      current_song = current_song.get_next_song()
      counter += 1
    
    return counter



  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    current_song = self.__first_song
    song_num = 1

    while current_song.get_title != None:
      print(f'{song_num}. {current_song.get_title().capitalize()}')
      song_num += 1
      current_song = current_song.get_next_song()

  