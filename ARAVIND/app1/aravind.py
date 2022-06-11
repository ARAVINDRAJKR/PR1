from django.core.paginator import Paginator


List=['aravind','adarsh','aslam','anandhu']
Split=Paginator(List,2)
print(Split.count)
print(Split.num_pages)
a=Split.page(1)
print(a.object_list)
b=Split.page(2)
print(b.object_list)
print(b.start_index())
print(a.start_index())
print(a.end_index())
print(b.end_index())
print(a.next_page_number())
print(b.previous_page_number())



