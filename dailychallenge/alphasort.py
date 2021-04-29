def alphasort(string):
    string = string.replace(",","") ## removes commas
    
    string = string.split(' ') #turns the string into a list using white space as a splitter

    string = list(dict.fromkeys(string)) #turns the list in to dictionary to remove duplicates and back into a list

    string = sorted(string,key=str.lower) #sorts the list alphabetically ## key=str.lower treats capital letters normally

    string = ' '.join(string) #turns the list in to a string

    return string
