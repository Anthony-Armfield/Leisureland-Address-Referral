

prefix = '<a href="">'
suffix = '</a>'

with open(r'H:\Work Related\Technode\LeisurelandRVCenter\Python Programs\address_ref_src.txt', 'r') as src:
    with open(r'H:\Work Related\Technode\LeisurelandRVCenter\Python Programs\dest.txt', 'w') as dest:
       for line in src:
           dest.write('%s%s%s\n' % (prefix,line.rstrip('\n'),suffix))

