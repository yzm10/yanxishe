# 数据增强
import PIL.Image as Image

def add(path):
  for root, dirs, files in os.walk(path):
    cnt = len(files)
    for i in range(800-cnt):
      f = files[i%cnt]
      im = Image.open(os.path.join(root, f))
      new_im = transforms.RandomHorizontalFlip(p=0.5)(im) # 水平翻转
      new_im.save(os.path.join(root, f[:-4]+'_'+str(i)+'.jpg'))

add('./train/-0_Frida_Kahlo')
add('./train/-1_Edgar_Degas')
add('./train/-2_Pieter_Bruegel')
add('./train/-3_Vincent_van_Gogh')
add('./train/-4_Rembrandt')
add('./train/-5_Henri_Rousseau')
add('./train/-6_Henri_Matisse')
add('./train/-7_Joan_Miro')
add('./train/-8_Titian')
add('./train/-9_Paul_Gauguin')
add('./train/10_Pierre-Auguste_Renoir')
add('./train/11_Marc_Chagall')
add('./train/12_Raphael')
add('./train/13_Leonardo_da_Vinci')
add('./train/14_Amedeo_Modigliani')
add('./train/15_Sandro_Botticelli')
add('./train/16_Pablo_Picasso')
add('./train/17_Rene_Magritte')
add('./train/18_Vasiliy_Kandinskiy')
add('./train/19_Salvador_Dali')
add('./train/20_Michelangelo')
add('./train/21_Mikhail_Vrubel')
add('./train/22_Paul_Klee')
add('./train/23_Camille_Pissarro')
add('./train/24_Giotto_di_Bondone')
add('./train/25_Gustave_Courbet')
add('./train/26_Gustav_Klimt')
add('./train/27_Henri_de_Toulouse-Lautrec')
add('./train/28_Francisco_Goya')
add('./train/29_Jan_van_Eyck')
add('./train/30_Andrei_Rublev')
add('./train/31_Andy_Warhol')
add('./train/32_Alfred_Sisley')
add('./train/33_Paul_Cezanne')
add('./train/34_Diego_Velazquez')
add('./train/35_Edouard_Manet')
add('./train/36_Peter_Paul_Rubens')
add('./train/37_Claude_Monet')
add('./train/38_Kazimir_Malevich')
add('./train/39_Hieronymus_Bosch')
add('./train/40_Caravaggio')
add('./train/41_Piet_Mondrian')
add('./train/42_Diego_Rivera')
add('./train/43_El_Greco')
add('./train/44_William_Turner')
add('./train/45_Georges_Seurat')
add('./train/46_Jackson_Pollock')
add('./train/47_Edvard_Munch')
add('./train/48_Eugene_Delacroix')