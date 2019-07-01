# -*- coding: utf-8 -*-

import parse_xml


if __name__ == "__main__":
  #1. 读取xml文件
  tree = parse_xml.read_xml("../sampledata/Outbound_Amazon_QA1.xml")

  print tree

  #2. 属性修改
  #A. 找到父节点
  nodes = parse_xml.find_nodes(tree, "vbr")

  print nodes
  #B. 通过属性准确定位子节点
  result_nodes = parse_xml.get_node_by_keyvalue(nodes, {"name": "vbrExternalId"})

  print result_nodes
  #C. 修改节点属性
  parse_xml.change_node_properties(result_nodes, {"vbrExternalId": "123"})
  #D. 删除节点属性
  parse_xml.change_node_properties(result_nodes, {"value": ""}, True)
  #3. 节点修改
  #A.新建节点
  a = parse_xml.create_node("person", {"age": "15", "money": "200000"}, "this is the firest content")
  #B.插入到父节点之下
  parse_xml.add_child_node(result_nodes, a)
  #4. 删除节点
  #定位父节点
  del_parent_nodes = parse_xml.find_nodes(tree, "processers/services/service")
  #准确定位子节点并删除之
  target_del_node = parse_xml.del_node_by_tagkeyvalue(del_parent_nodes, "chain", {"sequency" : "chain1"})
  #5. 修改节点文本
  #定位节点
  text_nodes = parse_xml.get_node_by_keyvalue(parse_xml.find_nodes(tree, "processers/services/service/chain"), {"sequency": "chain3"})
  parse_xml.change_node_text(text_nodes, "new text")
  #6. 输出到结果文件
  parse_xml.write_xml(tree, "../output/Outbound_Amazon_QA.xml")