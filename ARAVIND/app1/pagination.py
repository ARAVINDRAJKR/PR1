from django.core.paginator import Paginator
list1=['aslam','tom','habeel','ashkar']
split=Paginator(list1,2) #split
print(split.count)
print(split.num_pages)
page1=split.page(1)
page2=split.page(2)
print(page1.object_list)
print(page2.object_list) #display page contents
# print(page1.has_next())
# print(page2.has_next())
# print(page1.has_previous())
# print(page2.has_previous())
# print(page1.next_page_number())
# print(page1.start_index())
# print(page2.start_index())
print(page2.end_index())
print(page1.end_index())
