import yaml
import xml.etree.cElementTree as xml_tree
with open('feed.yaml','r') as file:
    data=yaml.safe_load(file)
    rss = xml_tree.Element('rss', {
    'version':'2.0',
    'xmlns:itunes':'https://www.itunes.com/dtds/podcast-1.0.dtd',
    'xmlns:content':'http://purl.org/rss/1.0/modules/content/'})
chaneel=xml_tree.SubElement(rss,'channel')
link=data['link']
xml_tree.SubElement(chaneel,'title').text=data['title']
xml_tree.SubElement(chaneel,'format').text=data['format']
xml_tree.SubElement(chaneel,'subtitle').text=data['subtitle']
xml_tree.SubElement(chaneel,'itunes:author').text=data['author']
xml_tree.SubElement(chaneel,'description').text=data['description']
xml_tree.SubElement(chaneel,'itunes:image',{'href':link + data['image']})
xml_tree.SubElement(chaneel,'language').text=data['language']
xml_tree.SubElement(chaneel,'link').text=data['link']
xml_tree.SubElement(chaneel,'itunes:category',{'text':  data['category']})

for item in data['item']:
    item_ele=xml_tree.SubElement(chaneel,'item')
    xml_tree.SubElement(chaneel,'title').text=item['title']
    xml_tree.SubElement(chaneel,'itunes:author').text=data['author']
    xml_tree.SubElement(chaneel,'description').text=item['description']
    xml_tree.SubElement(chaneel,'itunes:duration').text=item['duration']
    xml_tree.SubElement(chaneel,'pubDate').text=item['published']    
    xml_tree.SubElement(chaneel,'title').text=item['title']

    enclose=xml_tree.SubElement(item_ele,'enclosure',{
        'url': link +item['file'],
        'type':'audio/mpeg',
        'length':item['length']
    })
output=xml_tree.ElementTree(rss)
output.write('pod.xml',encoding='UTF-8',xml_declaration=True)