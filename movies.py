import csv

class Movies:

  def thousand_best_movies(self, query=None,
                                 publication_date_one=None,
                                 publication_date_two=None,
                                 order=None):

    data = self.thousand_from_file()

    if publication_date_two is None and publication_date_one is None :
      return [] 
    results = self.publication(data, year1=publication_date_one, year2=publication_date_two)
    return results

  """ this function filter the movies dataset by years """
  def publication(self, data, year1=None, year2=None):
    if year1 is None and year2 != None:
      return [m for m in data if self.year_in(year2, m)]
    elif year2 is None and year1 != None:
      return [m for m in data if self.year_in(year1, m)]

    return [m for m in data if self.years_between(year1, year2, m)]


  def year_in(self, yearq, row):
    flag = False

    if row.has_key('year'):
      year = row['year']
      flag = yearq == year

    return flag

  def years_between(self, year1, year2, row):
    flag = False

    if year1 < year2 and row.has_key('year'):
      year = row['year']
      flag = year >= year1 and year <= year2

    return flag

  """  reads the csv movies data and transfor it in a dictionary """
  def thousand_from_file(self):
    movies = []
    reader = csv.reader(open('greatest_films_of_all_time.txt', 'rU'), dialect=csv.excel_tab)

    for row in reader:
        data = {}
        data['title'] = row[0]
        data['director'] = row[1]
        data['leading_actors'] = row[2]
        data['year'] = row[3]
        data['category'] = row[8]
        data['country'] = row[7]
        data['summary'] = row[9]
        movies.append(data)

    movies.pop(0)
    return movies

