file=open('even_lines.txt', 'w')
file.write("-I was quick to judge him, but it wasn't his fault.\n")
file.write('-Is this some kind of joke?! Is it?\n')
file.write('-Quick, hide here. It is safer.')
file.close()

text_file=open('even_lines.txt', 'r')
result=''
count=-1
for line in text_file:
    result = ''
    count+=1
    for ele in ("-", ",", ".","!","?"):
        if result:
            result=result.replace(ele, '@' )
        else:
            result=line.replace(ele, '@' )
    if count%2==0:
        print(*(result.split()[::-1]), sep=' ')
