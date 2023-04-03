import math
import lvgl as lv


LV_PART_KNOB_CENTER = 0x090000
LV_PART_KNOB_RING = 0x0A0000
LV_PART_KNOB_GRIP = 0x0B0000

ui_img_gradient = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\xc8\x00\x00\x00\xc8\x08\x06\x00\x00\x00\xadX\xae\x9e\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x0e\xc3\x00\x00\x0e\xc3\x01\xc7o\xa8d\x00\x00(oIDATx^\xed\x9dk\xac\xad\xddU\xd7\xfb\x96\xb6\xdc,-\x02-\xd4B\x01iA\xa0\x04(\xd8\x12S\x11\x12P\x834\xd8*\xe1\x03\x05\xb4*\xa9A\xa3\xe0\x07P\xfc FM\x0c\x1ao\xa0x\xe1\x16\r\t\xd8\x04M\x8aD4\x94\xd8\x14k\xa1U\xa4\x15h\xb9\xb4\xb4\\\xdaBK\xaf\xf4\xc6q\xfc\xd6^\xe3\x9cq\xc6\x19s\xcc1\xe73\x9f\xb5\xd7:g\xff\x92\xff;\xc6\xfc\x8f\xf1<g\xef\xb5\xe6x\xd7}\xed\x87\x1ev\xc3n\xdc\xbau\xeb\xe1\x12\xd0\xa3D\x1f"\xfa`\xa7\x0f:\xea\x91"\xf0\xd7\xc7{\x8f\xf1\xfd\xa2\xf7\x88~\xf7\x18\xd1\xbbE\xef\x13}\xe0\xa1\x87\x1e\xfa=\x897\xec\xc0\xcd\x80,@\x06\x81M\xce\x86\xff}\xa2\xc7\x8a\x1e-\xfap\xd1\x87\x89>T\xc4\x80pY\xeb\xe5]\xcd5\xb6<\x06\x06\xbdS\xf4\x0e\xd1\xef\x88~[\xf4V\xd1\xbbep\x18\xac\x1b6\xa0\x17\xf8\r\x03\xc8@\xb0\xe9\x1f#\xfa\xfdG1\x18\xdcB<B\x04~#\xc3L\xaeq\xb4\xfe\x01\x11\xb70o\x13\xbdQ\xf4\x1b\xa27\xcb\xc0\xbc]\xe2\r\x03\xe8\x05{C\x82\x0c\x04\xb7\x0e\x1f#\xfah\x11\x03\xc1-\x03\xc3\x10mNhy\xa3\xb9\xc6J\xae\xb1\x95sk\xc2\x80\xfc\xba\xe8\xf5H\x06\xe6]\x12oH\xd0\x0b\xf0\x06\xc3\xf1\xb1\x03w\x93\x1e\'z\xbc\x88\xbbMxv\xc3i\xac\xe4\x1aGs\x8d\xa3\xb9\xc6\xac~K\xf4&\xd1\xaf\x88^+z\xa3\x0c\x0c\xb7<7\x18\xf4\xc2z\xe01C\xf1q"\x86\x82\xbbM~c\xd9\\\xe3h\xae\xb1\x92k\xdc\x92k\xec\xd5\xb9;\xf6\x1a\xd1/\x88\xdet\xf3\xf8\xe5\n\xbd\x80\x1eXd0x0\xcdP|\xac\x88\x01\xf1\x1b\xa8\x92k\x1c\xcd5Vr\x8d\xa3\xb9\xc6j\xce-\xcb[D\xaf\x16\xfd\x9c\x0c\xca\x9b%>\xb0\xe8\x85\xf3@!C\xc1\xb3N<\x9ex\xa2\x88\xc7\x14\xac\xa3\xcd\x02-\xaf\x95k\xac\xe4\x1aGs\x8d\x95\\\xe3L\xce\xad\xc8\x1bD?#z\xcd\x83x\xab\xa2\x17\xc8\x03\x81\x0c\x06O\xb7~\xbc\x88\xc1\xe0\x81w\xb4) \xcb5\x8e\xe6\x1ag\xeb\xad\\c%\xd78\x9a\x03O%3(\xaf\x90A\xe1)\xe5\x07\x02\xfd\xe5\xefk\x8ew\xa3\x18\x8c\'\x88z\xb7\x166\xd78[\xb7\xb9\xc6\xd1\\\xe3l\xbd\x95k\xac\xe4\x1a\x11/N\xbeR\xf4r\x11\x8fU\xb8Kv\xdf\xa2\xbf\xfc}\x89\x0c\x06\x0f\xb4?Q\xc4\xb3Q\xfa,\x94\xbd\xc25Vr\x8d\xb3u\x9bk\x1c\xcd5Vr\x8d\x95\\\xe3H\x9dW\xefyP\xff\x12\x19\x12\x9e:\xbe/\xd1_\xf8\xbe\xe2x\x8b\xf1$\x11\xcfF\xcd\x0c\x86\xc6\xd9\xba\xcd5Vr\x8d\xb3\xf5V\xaeq\xb6\xde\xca\x81\xa7\x86y@\xffb\x19\x14^\x94\xbc\xaf\xd0_\xf2\xbe\xe0\xf8\x18\xe3\x93D<#\xa5w\xa5\xc0_\xb16\xd78[\xb7\xb9\xc6\xbd\xea\xad\\c%\xd7X\xc95Vr\x06\xe5U\xa2\x17\xc9\xa0\xf0\x96\x97\xfb\x02\xfd\x05/\x1a\x19\x0c\x86\x81\xc7\x17\xdc\x9d\xd2W\xb8\xc1_\x896\xd78R\xd7X\xc95\xce\xd6m\xae\xb1\x92k\xac\xe4\x1a+\xb9\xc6^\x9d\xc7(/\x11\xfd/\x19\x14\xde\'v\xd1\xe8/v\x91\xc8`\xf0\xf3\x7f\x94\xe8\x93E\xbc\xfd\xc3^Q\xad\\c\xcf;e\xdd\xe6\x1ag\xeb6\xd7X\xc95Vr\x8dY\xce\x9b&_$z\xa5\x0c\xca\xc5\xbe\xdbX\x7f\xa9\x8bC\x86\x837\x07\xfeA\x11\x03Ry\x1b\x88\xc6\x9e\xb7\xb5\xae\xb1\x92k\xdc\xab\xde\xca5\xeeU\xd7\x1cx \xff_dH\x18\x98\x8b\xc3\xfe"\x17\xc1\xf1V\x83\xc7\x18<\xd6\xe0s\x14\xf6\x8a\xd18\xe3\xf5\xea\x1a\xcf\xb5ns\x8d\xb3u\x9bk\xac\xe4\x1a}\xce]-nM^zi\xb7&\xfa\x8b\\\x042\x1c\xbc\xcd\xfc)"\xdej\xee\xaf\x048\x95\xd7\xabk\x9c\xad\xdb\\\xe3^u\x9bk\x9c\xad\xdb\\\xa3\xcd\x7fU\xf4\x9fdH.\xe6\xd9.\xfd\xe1\xcf\x9a\xe3\xad\x06\xafe\xf0X\xa3u\xab\xa1qO\xafW\xd7x\xa9u\x9bk\x9c\xad\xdb\\#\xe2\xd3\x90?*z\xf9%\xdc\x9a\xe8\x0f\x7f\xb6\xc8p0\x10\x0c\x06\x03\xe2/l\x88\xe2hm\xa4\xae\xb1\xe7\xf5\xea\x1a\xf7\xaa\xdb\\\xe3u\xd5}\xce\xab\xef?+z\xa1\x0c\xc9Y\xbfmE\x7f\xf0\xb3D\x86\x83W\xc2?U\xe4\x9f\xa1\xf2q\xb4vj\xefA\xaa\xdb\\c+\xe7\x81\xfb\x0f\xc9\x90\xbc\xee\xe0\x9c!\xfa\xc3\x9e\x1d2\x1c\xbc\n\xce\xb3T\xfe\x05\xbfV\\Y\x9b\xf1zu\x8d=\xef\x92\xea6\xd78Z\xe7u\x93\x17\x8a^&\x83rv\xef\xeb\xd2\x1f\xf6l\x90\xc1` x\xc1\x8f\xcfh\xf8\x0b\xb4\x17g{"Oc+\xd7\xb8\xca{\xd0\xeb/\x15\xf1t0\x8fQ\xce\x06^?8\x1bd8x\xab\xc8\xa7\x8bxU\xdc_\x80\x95h\xc9zF\x8e\x83\xac\xcf\xd2\xf34\x8f<K\xe4Y\xee\xa7\xba\xe6\xcf\x10}\x9d\xec\x01\x9e\xa1<\x1b\xcef@\xe4\x82\xe1)\xdc\xcf\x14\xf1\xf9o\xd0\x0bn6\xc2\xaa\x1aD\x9e\xd2\xf3f\x8eQF\xce\xb3\xb5\x1e1R\xef\x9d\xbfw.\x9e\x8c\xf9\x8b\xc7\xbb\xd7g\xc1Y\x0c\x88\\ |\xd4\xf5\xb3D\xbc\x0b\x17\xf4\x82\xdc\x1a-[k\x96\xa8?\xf3,3^\xf5\x18\xcbL}\xe4\xdf\x9c9\xbf\xa5U\xe7\xdbc\x9e/{\x82\xc7\x9f\xd7\xce\xb5\x0f\x88\\\x10\xbcU\xe4\xa9"\xee^\x81^p\xab#d5\xa5r\x9ce\x95\xa7y\xe4Y\xaa\xe7\xb1\xac\xacG\xac\xac\x93\xf3\xac\xe5\xf3do|\xce\xc1\xb9F\xaeu@\xe4\x02\xe0\xff\x16<\x8d\x1b}\xcao\x8f\x083=\x96j\xff\xa8g\x99\xf1\xaa\xc7Xz\xf5\x88S\xfd\x9b\xbc\xfe\xf5\x95\xb2G\x9e.\x9a\xf99\x97pm\x03"\xbf4\xf73y\xdbH\xf6\xb9\x8d=\xa2%\xeb\x19\xa9A\xe4)\xab<\xcd#\xcfR=\x8fe\xe6\x18\xcb\xcc\xf1\xbd:C\xf2l\xd1\x1f9\xac\xae\x81k\x19\x10\x19\x0e\xdel\xf8dQ\xeb5\x8e\xc8\xdb#BVS*5K\xd4\xbf\xc5\x8b\x88\xea=o\xcfc,+\xeb|\xbe\xe7+d\xcf|\xd1\xd5\xf2\xb4\x9c|@\xccp\xe8\xbf\xcd\x85a\x05>\xdf3\xc2\x96\x1e\x88<e\x85gk3\xe7\x9b9&b\xeb\xbf3S\x07\xfc?%{\xe7\x99\xa2V\xcf.\x9ct@\xe4\x97\xe3\xfdT\x9f"\xe2\xdf\xe5\x17\xd5_\xd6F\x9f{o\x8fh\x99\xe9\xb1D\xb5\xaa\xa7\xac\xf2Nu\x9e\xea9-\xa3u\xd6\xcf\x12=\xfd\xb0:\x11\'\x1b\x10\x19\x0e\x9e\xad\xd2\xc7\x1c\xc0/\xec\x05>\xd7\x18y{D\xd8\xd2\x03\x91\xa7d^\xef\x1c\xa3\x9e\xa5\xe7m9\x8f\xa5w\xcc\x96:w\xb7\x9e#{\xe9iW\xcb\xfd9\xc9\x80\xc8/\xf4\x11\x12\xfe\x90\xa8\xf7\x8d\xe8\xad\\\xa3\x15\xec\x15-Y\xcf\xaa\x9a\xe5\xd4\xde\xa9\xceS=\xa7%\xaa\xf3\xc0\xfd\xabdO\xf1\xec\xe7\xee\xec> \xf2\x8b\xe8+\xe4\x0c\x07\xf0K\xab\xa0\x9a\xfb\x98\xd5VF\xc8j\xca\xca\xda)=\xcb\x8cW=\xc6\xb2\xf5\x9c\x0c\toK\xe1-I\xbb\xb2\xeb\x80\xc8/\xc0\x8b\x7f\x0cG\xebk>\xfd\x1a\xb2\xdc\xc7\xac\xb62\xc2\x96\x1eK\xe58\x88<\xe5\x1c\xbc=\x8e\x199\xa7\xbe\x98\xf8\x91\x07g\'v\x1b\x10\xf9\xc1y\xac\xc1\x1b\x0f\xed7\xa6\xab\xc0{*\x88r\xefi\x8c\xbc=\xa2ekO\xe58\xcbl\xbf\xc5z[\xce\xb7\xe71\x96\xca9y\xa1\x99[\x12\xee\xa5\xec\xc2\x9e\xb7 \xbc\xf1\x8coN\x07~\x99L\xd0ZC\xc5k\xd5\xf6\x88\xb0\xa5\xc7R9\xceR\xed\xcf<\xcb\x8ac-\xa7:Fa\x9f=[\x86$\xeb\x99f\x97\x01\x91\x1f\x96\xcfr|\x82\x88\x1f\xda\xff\xf2\xd6\xcb\xd6\x91\xc0\xe7>f\xb5\x95\x11*=J\xd63r\x1cT=\xe5\xd4\xde\xa9\x8f\xf9\x02\xd1\x1f\xbdJ\xd7\xb2|@d8x\xc6\xea\xd3D\xfc\xf0=Ak\r\xbd\xdc{\x1a#o\x8fh\xa9\xf4\xae\xaaY2\xafw\x8e\xaa\xa7\xf4\xbc\x99c"f\xfe\x9d?-{o\xf9;\x80\x97\x0e\x88\xfc\x80\xfa\xa0\xdc>\x9dk\x05=\x0f\xaa\xb9\xc6\x96\xd7\xaa\xed\x11\xa1\xd2\xa3\xac\xacU\xfa-\xa3\x9e\xade\x9e\xa5\xe7m9\x8fE\xeb<\xb3\xf5\xb5\xb2\x07\x97~\xe0j\xd9\x80\xc8\x0f\xc6\x0f\xcas\xd3\xf6o\xfbE\x82\x9e\x07\xd5\\c\xe4i\xccj+#\xac\xe8\x85\x91\x9a\xa5\xda\x1fy\xca\x9e\xde\x9e\xe7\xe1\xaf\x86\xf1\x0e`}1z3+oAxN\xda~\x8e<\x13T<\x15d\xb9\xc6\xc8\xd3h\x05{EK\xa57\xab)\xa3\xb5J\xbfe\xcb9\xaa\xc7\xda\\\xe9y3\xe7\xe13$\xcb\xde\xfd\xbbd@db\xf9$ \x8f;8\x1f?lE\x10\xf9*\x88|\x04#\x9e\x8d\xd0\xaa\xad\x8c\x95\x1eO\xd63R\xb3\xcc\xf6[\xb2sXVy[\xcf\xc3\xe3\x91?p\xb5\xdc\xc6\xe6\x019\xde\xb5\xe2q\x07\x8f?\xc8\xb7\x08Zk\xb0\xb5\xc8\x87\x8a\xd7\xaa\xad\x8c\x11\x95cNQ\xb3T\xfb#O\xe9y\xd1\xb1\x99g\x99\xf1x]\xe4\xb9+\xeej\xad\xb8\x05\xe1\xe9\\\xde\x88\xc8\x0f8*\xe8y0\x93k\x8c<\x8dV\xb0g\xac\xf4(YMYY\xab\xf4[\xaa\xe7\xc8\x8e\xb5\xccx\x9aG\x1e\xf0\xd5Q_|\x95\xce\xb3i@dBy\xb9\x9f\x07\xe6\xfc`\xb3\x82\x9e\x073\xb9\xc6\xc8\xf3\xb1\xd2\xb3%ZV\xf4Z\xb6\xd6,Q\xff\xec9,3\x9e\xe6\x91giy_&{\x94\x8fXL3= \xc7\xbbV\xbc\x95d\x8f\xbbV=A/\xafx>f\xb5\x95\x11V\xf6\xc2\xaa\x9a%\xf3z\xe7X\xe1Yf<\xfe\x07\xce;\x7f\xa7\xefjm\xb9\x05\xe1\x93\x81\xd9\xb3V\x9e\xa8\xc7\nf\xd7\xe0s\x8dUO\xa3\x15\xec\x15a\xa4W\xc9zfkJ\xe58\x88<\xe5\x1c<\x9b\x7f\x86\xe8\xf3\xaf\xd2q\xa6\x06D&\x92\x17\x02\xf9|\x07?HK\x9c\xdb*\xea\xe9\t\xaak\xb05\xefA\xcf\xf3\xb1\xd2\xb3%ZF\x8e\xc9j\xcaH\xcd\xf6T\x8e\xb3T\xcf\xb1\xc5S\xaa\xc7Z\xd8{\xcf:>\x1c\x18\x86\x83g\xe0\xaf;\xf1\x96\x92\xd9\x8d\xdf\x12\xf4<\xb0\xebH\x10\xe5\x15\xcf\xc7\xac\xb6*Vzl\x84-=\x96\xd1\xe3"O\xd9\xcb\xb3\xb5\x99\xf3\xf1\xae\xdf/\xb9J\xc7\x18\x1e\x10\x99D\x9eB\xab>0\x8f\x88\xfa\xac\xa0\xe7\xc1L\xae\xb1\xeai\xb4\x82\xd5\xd1\xb2\xf2\x18K\xd63r\x1cx/\xabA\xd5S\xf6\xf0\xbeT\xf6.\xaf\xb4\x0f1s\x0bR}`\x0e-\x1f\xa2\x9a\n*\x9e\n\xaa\xb9\xc6\xaa\xe7\xa3\x15\xac\x8e\x96\x91c\xb6\xf4\xc0H\xcd2\xdbo\xa9\x9ec\x8b\xc7\x1f}}\xceUZgh@d\x02\xb9[e\xdf\xc6\x8eZw\xb3\xf03E\xc7\x8c\x08Zk\xc8r\x8dU\xaf\x15+=\xb3\xb1\xd2c#Tz\x94\x95\xb5=\xfa-\xab\xbc\xcf\x95=\xfc\xa4c^\x82\x8d:\x02o\'\xf1\xef\xd4\x05\xbb\xf6\xca\x88\xfaU\xd0\xf3\xa0\xb5\x86(\x8f<\xf0^\xab\xe6c\xa5g&Z\xf68\x06\xb2\x9aR\xa9YV\xf4W=\xa5z,\xef\xf8\xe5\xb5\x91\xe8\x1c!\xe5\x01\x91\x93\xf2\xd9\xdf\x8f\x17qr\xab\xec\xd6\x00"_\xa5D5\x04=\x0f\xec\xda\n2\x0fl\xcdz\x1a#\xcf\xc7J\xcfl\xac\xf4D\xd1\x92\xf5\xb4j\x95\x1e\x88<\xa5\xda\x1fyJ\xe6E\xe7\xb0D\x1eof,\x7fn\xa44 \xc7\x89\xf3_\xdb\xb3R\x10\xf9\x08z\x1e\xb4j\x91\x0f>\xd7X\xf5|\xb4\x82U\xd1R=\xc6G\xc8jJ\xd6\xb3\xaaf\xc9\xbc\x99sT\xfa\xd8\xc3\xdc\x8a\x94\xf6~\xf5\x16\x84\xc7\x1eO\x14\xf1\x8f\x8c\x88\xf3g\xb70\xaa^\x0f\xf4<\xd8\x9akly\xad\x9a\x8fV\xb0"Vz\xb2\x08[z,\xa35\xefe5K\xe6E\xe7\xb0d}\xfc-\x1a\x1eKw\xa9\x0e\x08\xdf\x88ho=*\x9b^\x05\x91o\xa5D5\x15D~K0\x92G\x1eD1\xab\xd9\x08\xd5\xde^\x8c\xa8\x1e\xab\xd1\xb2\xb5g\xa4f\xa9\xf4g5\xa8z\x8a\xf7x\xeb\xc9\x97^\xa59\xdd\x01\x91\x9b"^\xf7\xe0\x9b#\xf8GZj\r\x0cD~K\x10\xf9-Au\rY\xae\xd1\xe7\xde\xd3\x18y>Z\xc1\xeah\xa9\x1e\xa3\x11\xb6\xf4X\xb6\xd6,\xb3\xfd\x96\xe8\x1c\xde\xfb\xc3\xb2\xb7\xbb\xaf\x8bTnA\xf8&v\x1e\xfds\xe2SHi\xd5z\x1e\xd8uK\x90y0\xe3\xb5\xa2\x15\xac\x8c\x9a+Y\xaf\x8d\x96\xad=\xabj\x96j\x7f\xe4)-\x8f=\xdd}u=\x1d\x10\x990n\x8a\xb8{\xc5\t\xd1\xc8]\xab\xad\x82\xaa\x0f\xad5D\xb9\x15d\xb9\xc6\x96\xd7\xaa\xb5\xa2\x15l\x8d\n\xeb^o+\xc2\x96\x1e\xc8j\xcah\xad\xd2o\xa9\x9e\x83\x9c?\xa7\x90\xbeG\xabw\x0b\xc2\x03sN\xc0\xc9\xbc\xfc\xb0D\xc3\xb3\xd7@A\xe4\xb7\x04[s\x8dV\xe0k0\x12\xad`k\xb4T\x8f\xd1\x08[z,Y\xcfH\xcd2\xdbo\xb1\x1e_0\xf2yWiLo@x\xcf\x15=\x95\x8d\x0e\x91\xbfE\x10\xf9\x08f\xd70\x92{Oc\xcbk\xd5\xb2\x08\xe4*\xd8\x12+=Q\x84J\x8f\x92\xf5\xcc\xd6\x94\xcaq\x96j\xbf\xf5\xbePnEl\xed.\x9a\x03"\x07\xf1\xf7\xca\xf9\xcc\x07\x07Wt\x0e\xb7\x16P]C5\xd7X\xf54f5\x1fUJ\xd43\x12-\xd5c4Z*\xbdYM\x19\xa9\xd9\x9e\x8a\xd7\xebW"\x8f\x17\r\x9bO\xf9f\xb7 \x1cx\xca\x07\xe7\x99\xa0\xeaCu\r\xbd<\xf2\xa0\xe7i\xccj\xadX\xe9\xa9F\xcd\x95\xac7\x8a\xb0w\x0fd5%\xf3l\xcd{Y\x8d\x97/\x9ey\x95\xdeK8 \xc7\x07\xe7|\xe6\x83\x93x\xd9[\x8a\xca\xad\xc6^\xb7,*\xe8y`\xd7V\x10\xe5\x91\x07>\xd7\x18y\x1a\xb3Z+Z\xc1lTX\xf7z[\x11*=\xcaL\x8f%;\xber\x9c\xa5r\x8e\xa7\xc9\x9e\xe7Ot\xdcC\xeb\x16\x84o)\xe1.\x16\'8\x17A\xe4#\xe8y\xd0\xaaER4\xb7\xbe\xe6\x15OcV\xebE+\x98\x89\x9a+Yo\x14ae/\x9c\xa2\x06\x91\xa7\xe0\xf1\x81\xaa\xf0\xfdY\xad\x01\xa1\xd9\xff\x9f\xff\\o-T\x10\xf9-A/\xb7\x02\x9fk\xacz\x1a\xb3Z\x16\xa1\xda\xeb\xa3\xc2\xba\xd7\xdb\x8a\x96\x15\xbd\x96=k\x96\xa8\x9f\xfc\x19W\xe9\xdd\xdc3 \xc7\xbbW|\xa7\x10\x07\xa1\xbd7\xfd\xa8\x94Vmv\r3\xb9\xc6\xaa\xa7\xd1\nz\x11\xaa\xbdY\xd4\\\xc9z\xb3\x08+{\xe1\x145\x8b\xad\xf1Y\x11>\x08x\x17\xf7\x0c\x88\xa0w\xaf\xaa\x83Q\xe9\xbb\xce!\x83\xea\x1aF\xf2\xc8\x03\xef\xb5j\x1a\xb3\x9aF+\x98\x8d\n\xeb^o/\xc2\xca^\xc8j\xcah\xcd{Q\x8d}\x7f\xcf\xdd\xach@\xf8\xc4\x15\x07e\xca6\xfc\xa9\x86\x01\xaa>dk+\xe8\xe5\x91\x07\xb6f=\x8d\x91\xa71\xab\xf9h\x053QsOvL\x14-+z-Y\xcfH\xcd\x92\xf5\xf3Y\x91\xbb\x98\x1d\x90L\x10\xf9{\x08F\xfc\x96\xa0\xb5\x06\x9fk\x1c\xa9k\x8c<\x8dVP\x89V\x10\xad}\xd4\x1cZ>\xd8Z%\xc2\xca^8EM\xf9\xecc\xbc\xcd]\x03"\xf7\xc1x\xe7._\xd5\xc8\x81\x91*\xb7\x0e\xa7\xba\x05QA\xc5\x87\x91uO\x90\xe5\x1a\xab\x9e\x8d\xd0\xeb\x89\xa2J\xf1^T\xd7\xe8}[\x1b\x89\x96\x15\xbd\x90\xd5\x94\x15\xb5\'\xca\x0c\xf0\x8c\xd6m\xfc-\x08\x1f\xa9\xe5\x85\x13\xbf\xc9O\xbd\xe9\xf7\x12T\xd70\x9bG\x1exo\xa6V\x89@\xde[\xdb\xa8\xf8>\xf0\xbd\xd5\x08+z-3=P9\x8e\'\xa8\xf80\xd5m\xa2\x01\xe1@U6\x18\xb6v\xdd\x03\x04U\x1f\xaak\x98\xc95\xfa\xdc{\x1a#OcVkE\x95\x12\xad[\xd1\xf7E=#\x11Fz\x95\xac\xa7U\xcbz,\xd9qO=\xc6\x03~@f>V\x1b)\x1a\x98\xbd\x87\x08\xaa>T\xd70\x93k\xdc\xe2i\xccj\xbd\xa8R\xa2\x1e\x1b\x15\xd6\xbd\xdej\xb4\x8c\x1c\x93\xd5\x94\xacg\xa6\xf6\xe4\xe3K\x1d\x07n\x0f\x88\x98\xfc\xc1\x7f>{Nc\xa6\xd9\x8d\x0e\x91\xef\x15\x11\xf5E\x82\xaa\x0f\xd9\xda\nF\xf2\xc8\x83\x19OcV\xabF\x9f\xdb\xb5\x8f\x9a+Y\xefH\x84\x95\xbd\x90\xd5\x94j\x8d\x978\x1e\x7fX\t\xf6\x16\x04\x93\x17JF\x06`\xe5\xad\x82\x92\xd5 \xaa[\xc1\x88\xdf\x12D>\x82(\x8f<\xf0\xb9\xc6\x967S\xabD \x8f\xd6\xea\xb5\xea\xb0*\xc2H\xaf\x92\xf5\xb4j\x95\x1e\xd0\x9c\x19\xe0#\xe6\x07\xec\x80\xf07\xddhR\xf9\xcd\xdf\x1b\x86\x15\xf5\x8a\xa2cg\x05\xd55\xd8\x9a\x15\xd8\x98\xe5\x91\x07Q\x9c\xad\xb5\xa2J\x19]\x83\xae\xb7F\xcb\xc81YM\x99\xe9\xb1\xf09\xa8\x03l8\xa5\xf5\xb7>Vo\xca\x8a2\xa2~/\xa8\xfaP]C\x94[A\x96k\xf4\xb9\xf74F\x9eF+\x18\x89*ed\xbd2Vzl\x84\xbd{n\xbf\xa2~\x18\x10y\xfc\xc1\xe7>\xf8\xe6D\x1aVif\xb0\x94\xa8\xa6R\xa2\x9a\x15T}\xc8\xd6V\xb05\xd78\xe2\xb5j\x1a\xb3Z/\xaa\x94\xde\x1at\xbd5ZV\x1ec\xc9z\xa2\xda\xe3d&\xf8\xcb\xcd\xb7oAX\xf0\xf9\xdc\xea\xa6n\xf5\xcd\x0c\xc5\xac\x94\xa8\xa6\x82\x11\xbf%h\xada$\x8f<\xe8y\x1a{5\x15\xccD\x15\xf85\xf8\xfa\xca\x08\xd5^\x8d\xb0\xa5\xc7\xa2\xdecD<X\xbf= \xbcQ\xab\xf2\xb5\xa2\xd1\x00\x8c\x0cE\xaf\x97z\xf5|\xd5^\xa8\xf80\xb2\xb6\x82j\xae\xb1R\xcfj\x90\xc5J\xcfhT\xc1^\x11\xaa\xbd\x1a\xa1\xd2\xa3d=\xe4\xec+^\x13<$\xe0\xdf^\xa2\x1b\xaf\xb2\x01W\x0b"\xdf\xcb\x12\xd5\xad\xa0\xe2Cu\r\x95\x1a\xf8\\\xa3\xcf\xbd\xa7\xb1\xea\xf9X\xe99\xc7h\xd9\xe3\x18\xc8jp\xf83\t: \xbd\xbfs>;(\xa7\x1a0\x88|+\x88|/\xa8\xae\xc1\xd6Z\x82\xcc\x83Y\xafU\xd3h\x05\x97\x16\xa1\xda\xab\x11\xb6\xf6<\x81D\x07d\xe4\xf3\x1f\xaa=6?D~EJTS\xc1\x8c\x07\xad5\xf4r+\xc8r\x8dUOcV\xd3X\xe99\xc7h\x199\xa6\xd2\xa3\xf8\x1a\x0f\xd4\x1fz\xf8\xf1e\xf5\xca+\xe8U\xf5\x06\'\xabS\xdb2x\xb3\xc7B\xe4[A\xe4#X\x99klyY\r\xb2h\x05\xab\xa3R\xed\x1f\x8dp\x8a^\x9e\xd5}$\x1b\x8a\x07\xe7<\x83\x85\x89z\x9b,\xaag\xc7\x8cnZ\x88\xfc\x8a \xf2\xad\xa0\xe2+\xde\x8b\xf2\xac\x06#y\xc5\xd3\xd8\xf2Z5\x1f+=\xa3Q\x05{E\x18\xe9U*\xbd\x9a\xdf\x1e\x10\xbe\xee$\xfazQ\xdd\xd8>\x8e\n"\x7f/)QM\x05#~K\x10\xf9\x08fr\x8d[<\x8dYMc\xa5\xe7\x1c\xa3e\xe4\x98J\x0f0\x17\x8fe\xd3\x8f\xbc\xfe1\xa3=\xcf\x9d\t"_\x05\x15\x1f\xaak\xa8\xd4 \xca#\x0f*^V\x83,Z\xc1%\xc5J\x8f\x8dP\xed}\x0c\x9b\xb7\xf5\xe5\xd4\x15\xed\xb1\xf9W\x9e\x13"_\x05\x91\xef\x05\xd55\xd8ZK\x90y`k\xde\x83(\xb6\xbcV\xcd\xc7J\xcf9E\xcb\xeac>\x82\xcd\xc8\xab\xe8,\xd0\x96\xcdi\x8f\xed\x9d\'\xabC\xe4\xcf\n"_\x053\x1e\xd8\xb5\x15\xf4r+\xc8r\x8d>\xf7\x9e\xc6\xc8\xd3\x98\xd54Vz\xce1B\xb5W#\xb4j\x8ff\xa3f\x8f?\xaa\xebs\x17D\xbe\n*^&h\xadak\xaeq\x8b\xa71\xabi\xb4\x82K\x89P\xed\xd5\x08Q\xed\x9e[\x10\xafU\x83q\x0e\x03\x05\x91\xaf\x82\x9e\x07\xb3k\x98\xcd#\x0ff<\x8dV\x90\xc5J\xcf9E\xcb\x96c\x0e\x03\xc2\x07D0fu\x0e\x9b\xbf*%\xaa!\xe8y0\xb2\xb6\x82\x99\\\xe3H]\xa3\x15D1\xabi\xac\xf4\x9c[\xac\xf4D\x11\xc8?\x84\xcd\xad\x7f\xe2`\xf5F\xef\x9d\xafU\xdf{\xe0V\x9c\x1f\xaak\xa8\xd4 \xca#\x0fl\xad\xe7i\x8c<\x8dYM\xa3\x15\x9c{\x8c\x189\xf6\xf0:\x88\xff\x1b \xd5\r\x14\xf5\xed\xbd\xb9WH\x89j\x08f<h\xad\xc1\xd6\xac \xca#\x0f|\xaeq\x8b\xa71\xab\xf9h\x05\x97\x10+=6>\x8a\r\xcd[M*\x9b]\xd7\x970\x04\x15A\xe4#\x98\xf1\xc0\xae\xad \xca[\x82^\x1eyP\xf1fjQ\x84j\xefuGK\xe5\x98G\xb0\xd9{\x9f\x03\xa9\x0c\xc4\xaa\x9eS\x0b"\x1fA\xc5\xcb\x04\xad5l\xcd5V\xeaY\rFk\x1a\xad\xe0R"\xf4z\x0ew\xb1X\xec\xa5\xd9\xf3\x9f\xe30\xb5\x04#k+\xd8\x9ak\xf4\xb9\xf74V=\x8dV\x90E+8\xf7\x08i\x0f\x1b\x11X\xa0\xd1\x8d\x19\xf5\x8f\x9c\xe3\x1c\x06\x01"\x1f\xc1\x8c\x07\xad5Tj\xd0\xcb#\x0fVy>Vz4Vz\xce!Z|\xed\x03l\xd0\xf7\x8b0\xact\xe3\xae\xde\xc0\xd5\xf3A\xe4\xef%\x88|\x043\x1e\xd8\xb5\x15D>\x82\xaa\x0fY\xaeq\xc4k\xd54f5\x1f\xad\xe0\x9cc\xe4\xbd\x9f\r\xfb{\xc7EE\xd9\xe0\xac\x1e\xa6\xaazD\xc7D\x82\xc8GP\xf12Ak\r\xb66\xe2C\x94G\x1e\xf4<\x8d\xbd\x9a\nz\x11\xaa\xbd\xd7\x15-\xea\xbd\xd7\x0eH\xb6\xc1G7\xbf\xed\x9f\x19\x9c\x91c\xe8\xcd\x14\x1d\xb3J\xd0[CV\xdf+\xd7X\xa9\xcf\xd44f5\x8dVp\xce\xd1\xe6\x87[\x90\xf7\x1e\x17\xd7\xa5\x95\x9b\xd8\x12\xd5{RZ\xb5\x8a\x0fv\xed\x05\xad5\xac\xcc5\xfa\xdc{\x1a#O\xe3l\xcdG+8\xb7hy\x0f\x9b\xf3\x9d"\x8a*\xdd\xb0\xd5\x8d\xbbu\x83C\xe4Wei\xf9`k=\xc1\x88\xef\x05#k+X\x91G\x1e\xccx\x1a{5\x15T\xa2\x15\x9c[|[4 ^~\x00F\x07\xc8\xabu\xbe\x19A\xe4G\xb2Du/\xa8\xfa\xd0\xf3\xa0\xb5\x06[\xb3\x82\x91<\xf2\xc0\xd6\xbc\x07\xde\xcbj\x90\xc5J\x8f\x8fVp\x0e\xf1\xf6\x80T6\xe9\x96\x9e-C\xd0\x12D~EJT\xb3\x82\xaa\x0f=\x0f\xec\xda\n\xa2<\xab\x81\xe6\x91\x07>\xd7\xe8s\xefily\xad\x9a\xc6\xac\x96E\xa8\xf6\xee\x1d\xdf\xae\x03\x82\x81Vn\xe4\xad\xe7\xea\x1dO]\x15\xd53\xcd\x1e\xd7\x13D~K\xd0ZC\xab\x16\t\xaa\xb9\xc6-\x9e\xc6^M\x05\x95h\x05\xd7\x19\x0f\xb7 o?.\xacF7\xcf\xd6\xcd\xb6\xe5x\x88\xfcLJT\xf3\x82->\x8c\xac\xad\xa0\xe7\xc3H\x1ey0\xe3i\xccj\x1a+=>Z\xc1\xa9\xe3[\xd8\x98\xef\x10\xbdG\x849\xaa\xd9\x8d\xbdu\xa0T\x10\xf9U)Q\xcd\nF|/\xa8\xae\xa1R\x83\x99\\\xe3H]\xa3\x15Tk\x1a\xb3Z/Z\xc1\xde\xf1}\xa2\xc3\x80\x90D\xb7"H7\xb2\xdf\xd0\xd9\x06_\xb5\xf9{\x82\xc8\x9f\x11D\xbe\x15T}\xe8y`\xd7V\xd0Z\xc3l\x1ey`k=Oc\xe4i\x9c\xadU"T{\xb7\xc4\xb7\x88\x0e/\x14~@\xf4;\xa2\xca\xc6\xde\xb2\xf9g\x8e\xcd\x8e\xa1\xa6\x8a\xea#\xdaz\x0e\x98\xf1\xa0R\xf3\x82\x91<\xf2\xc0\xe7\x1a\xb7x\x1a{5\x15\x8c\xc4J\xcf\x8a\xc8\x80\xbc\xef\xe1\x0f=\xf4\xd0-I\xde,\xa2\x80Vl8Uv._\x9b\xfdw!\xf2G\xa4D5+\x88|\x04\x15\xcf\x0b\xa2\xbcW\xb3\x82,WZu\x9bk\xdc\xe2i\xccj\x1a\xad\xa0\x12\xad`\x8f\xf8Ff\x83M\to\x14a\xceH7\xf6\xe8\x06\x87\xc8\x1f\x11D\xfe\xac \xf2\xad \xf2\x11\xf4<\xb0k/h\xad!\xcaG\x05Q\x1ey\xe0=_\x8b<\x8dY\xcd\xc7J\x8f\x8fV\xb0*\xbe\x81\xff\xe8\x80\xbc^D\xc1j\xf6\xff\xe8\xa8r\xec\x96\xf3\xef)%\xaa\xa9 \xf2[\x82-k+\xd8+\xd7\xe8s\xefi\xacz\x1a\xb3\x9a\xc6JO+Z\xc1\x96\xf8K$: \xbf.\xea\xbd\xab\xd7o\xe8\x99\r\xbe\xfa\x18j3\xe7\xec\xa9rN\x18\xf1\xbd\xa0\xba\x86J\rf\xf3\xc8\x83U\x9eF+\x88\xa2\x15\x8cF\xa8\xf6F\x91\x87\x1d\xafe\xc1F\x80\xb7\x89x&+\xda\x18\xde\x1b\xdd\x90\xa3\xfd\xa3\x82\xc8\xdf"%\xaaYA\xd5\x07\xefyA\xe4#\x88|\x04[s\x8d>\x8f<\xa8x\xad\x9a\xc6\xac\xa6\xb1\xd2\xe3\xa3\x15\x8cF\x9e\xb4\xfa-\x92\xc3\x80\xc8\x83\x91\xdf\x95\xf0&\xd2\x8d\xda:<{\x0f\xd3\xa8\x94\xa8\xa6\x82\xaa\x0f\xd9\xda\x0bZk\xa8\xd4\xa0\x97G\x1e\xb4\xbc^\xdd\xc7\xd9\x9a\xc6JO+ZA%\xf2\x98\x9c\xd7\x07\xaf\x06\xe4\x087)\x14\xd1\xd6\x8d\xde\xf2.U\x10\xf9*\x88\xfcH\xb0j\r\xb6\xd6\x12Dy\xe4\x81\xcf5V\xeaY\rFk\x1a\xad`&ZA+\xbe\xfa\xf8\xec\xee]\x03\xf2j\x91\x1e\xbcZvXf\x06\';\xe6\x14\x838\xfbo@\xe4{\xc1\xec\x1azyKP\xcd5\xfa\xdc{\x1a\xab\x9eF+\xc8\xa2\x15\xccD+\xb0\xf1UW\xe9\xd5\x15\xafp\x0b\xc2\xab\xea\xf6@\xbf1z\xeb\xfbUJTSA\xd5\x87\x9e\x07\xd9\xda\n\xf6\xcc#\x0ff\xbdVMcV\xf3\xb1\xd2\x93E\xb0\x1e\xdf\xd1\xf0\xf3\x87\x95`\x07\x84\xc7 o\x15\xd1\xe4u\xdd\x83\x01\x91\x8f \xf2\xf7\x10D\xbe\n\xaa>\xf4<\xb0k+\x88|\x04+s\x8d>\x8f<\xf0^V\x83\xd1\x9a\x8f\x95\x9eV\xf4\x1e3\xc0\xcb\x1e\x07n\x0f\x88\xdc\xe7\xe2i\xde_\x14m\xdd\xfc\xa3\xc7_\xf7\xf0\x8d\n"_\x05U\x1f\xbc\xe7\x05Q>[\x83\x91<\xf2\xa0\xe5Y\x81\xaf\x81\xf7fj>VzZ\xd1\xea\xe7e\x16\xb8\x159p{@\x8e\xbcR\xe4\x0f\xa8*\xda\xd8\xad\xcd>:\x04\xe764JTCP\xf5![{Ak\r\xb6f\x05#y\xe4\x81\xcf5n\xf14\xce\xd64Z\xc1h\x84\x97\x1f\xe3\x01? \xffWT\xf9\x96\x93\x19\xed\xb5\xc9\xafkx\xf6\xfcwav\rQ\x9e\xd5@\xf3\xc8\x83(\x8f<\xa8xY\rFk>Vz|\xe4\x99\xab\x9f:\xac\x8e\xdc5 r\xd3\xc2\x8b#\xfem\'~#\xf4\xd6\x0f\x8a \xf2UP\xf5\xa1\xe7A\xb6\xb6\x82(\xaf\x08\xaa\xb9\xc6J=\xabA\xcf\xd3\x98\xd5|\xac\xf4\xd8\xf8k2\x03\xbfz\xcc\x0f\xdc5 G\xfe\xb7\x88\x03\xbcF\x06cthF\xce}NR\xa2\x1a\x82\xaa\x0f\xde\xf3\x82\xc8G\xd0Z\xc3^\xb9F\x9f{O\xe3\x887S\xf3\xd1\n\xb2\xf8\xd2\xab\xf4\x0elD\xcf+D\xb3\x1b4:\xee\xdc6{\x85\xe8\xb8L\x10\xf9\x08\xaa>dk/\xc8\xd6V\xb0:\x8f<X\xe5i\x9c\xad\xf9\xd8\xeb)\r\x08\xefb\xd4\xcf\x87\xec\xb9\xb9G\xcf\x9d\xf5\x8f\x9c\x8b\xde\x9e\xa2\xe3\xaeK0\xbb\x86J\rF\xf2\xc8\x03\x9fk\xdc\xe2i\xec\xd5T\x90\xc5V\x8d\xa7wy\x0c~\x17l\x86\xbb\x90\xfb`|\xd3\xe2O\x93&\xf2\x9b\xa8\xba\xa9\xb2\xbe\xd9s\x9e\x8b \xf2\x11T}\xe8yP]\x83\xadY\xc1L\xae1\xcb#\x0f*\xdeLMcV\xd3h\x05\xc4\x97\xc8\xde\x7f\xf7\xd5\xf2\x0el\xc2\x88\x97\x1c\xa3\x9eD7\xeb\xc8&\x1e\xdd\xe0\x90\xad3A\xe4\xb7T%:6\x13D>\x82\xaa\x0f=\x0f\xb2\xb5\x15D\xb9\x17Dy$\xc8r\x8d>\xafx\x1a#O\xe3l\xcdG\xcd\x7f\xfc\x18\xef\xa25 \xbc`\xf8\x9b"=\xc1V\xb5\x86\xc5\xfa\xbegt\xc0*R\xa2Z$KT\x8f\x04\x91\x8f\xa0\xeaC\xcf\x03\xbb\xb6\x82\xd6\x1a\xa2\xbc%\x18\xc9#\x0fVy\x1a{5\x15d\x91w\xef\xfe\xeca\xe5\x08\x07Dnj\xf8\x1a\xa0\x97\x91N\xa8\xb7\xb1\xb7l\xfc\xd6\xb1\xf8\x95\xf3j\x9fW\xa5\xcf\xf7\xcc\n\xaa>x/\x13dk+\xd8+\xd78R\xd7\xd8\xf2\xb2\x1ad\xb1\xd7\xf3\x93\xb2\xe7\xdfu\xcc\xef\x82+\xbe\xc5O\x88\xf8\xc6\x93\xea\xe6X\xb9\x89f\x04\x91\xdf\x92%\xab\x81\xaf\xf7\x04\x91\xaf\x82\xc8\x8f\x04\xab\xd6P\xa9\xc1\xd6\\\xa3\xcf#\x0f\xbc\x97\xd5\xc0{\xad\x9a\xc6V\x8d=\xfe\xa3W\xe9\xbdd\x03\xf2+"\xfb\x16x?\x00\x95\x81\x18\x1d\x9a\x99\x7fcTJTk\xc9\x12\xd5#)Q\rA\xc5\x8b\x04\xb3k\xa8\xd4`$\x8f\x04>\xd7\xe8s\xefi\xacz\x1aGk\xaf\x11\xfd\xbf\xc3*\x80\r\x18"79\xbc\xec\xfe\xdf\xaeV\xb7O\x8ef7\xf1\x1e\x9b}T\x10\xf9#R\xa2Z$\x88|\x04\xab<\xc8\xd6V\x10\xf9\x08z>\xd8\x9a\xf7 \xcb5\xae\xf64ZAV\xfb\x11\xd9\xeb\xbc\xbd*D\x9bBn\xdd\xba\xf5a\x12\xfe\x8d\xe8\xd1\x07\xe3\xea\xbd*\x95\x08\x99\x07\x95\x1c\xfc\x1a"\x0fZ~\xc4H\xaf%\xbd\xcc\x1ad\xc7\xb4j\x91\xef\xbd^O\xaf\xbf\xd5\xbbg>S\xcf\xbc-5\xbe\xb8\xfd\xcf\xca\x80\xf0\x19\xf4\x90\xe6-\x08\x1c\x1f\xb8\xf0\xf4\x17\'\xab\xe8\x1cn%*\x82\xc8\xafH\x89j-A\xe4#\xa8\xfa\x90\xad\xbd\xa0\xba\x86S\xe4\x1a}\x1ey\xd0\xf34\xce\xd4~,\x1b\x0e\xd0\xc6&r+\xf2x\t\xffJ\xf4H\x96xI\x84J\r*\xb9\xe2\xbd\xa8\x07Z\xbe\xa5\xd23J\xf7r<\x92\xf5\xb5j\xde\x8f\xfaz=\xd9\xbaZ[\x91\xcf\xd4WxQ\x8d\x07\xe7_-\x03\xf2\xba\xabeLz\x0br\x84\xe7\x88_,\xe2\xc4z\x0b\xd1\x8a\x91\xb2Z$\xdf\x0fv\xbdE\x10\xf9[\xa5D5+\x88|\x04\x15\x1f\xec:\xf2\xa0\xba\x06[\xb3\x82\x15y\xe4\x81\xady\x0ff\xbdJ\xed\x7f\x88\xeez\xe7n\x04\x9b1E&\x8c\xff\xe3\xfegQ\xef\x8b\xe5*j\r\xcb\xca\x01\xbbNA\xe4[A\xe4#\xa8\xf8`\xd7\x91\x07\xd9\xda\n\xa2<\xabA/\x8f<\xf0\xb9\xc6\x91\xba\xc6\xc8\xd3\xd8\xaa\xb1\x97\x7f\xf0\xb8\xb7S\xba\x03r\x84W\xd6{\xef\xcf\xf2\xeam\xec-\x1b\xbful\xe5\xdf\xdc\xf2\xef\xf6\xb4\xe7\xb9\xbd \xf2\xad\xa0\xb5\x86j\xcd\n\xaa\xb9\xc6J\xaeq\xa4\xae\xd1\n|\rl\xe4S\x83\xe1+\xe7\x1e\xae\xd0.2i\x87\x89\x13q\xbfM\xff\xd1\x96N\xb9If\x04\x91\xbfBJT\xb3\x82\xc8GP\xf5![\xb7<\x15D>\x82(\xaf\nl\xac\xe4\x1a}^\xf14\xf6<\xf6\xf0\xf7\xcb\x9e&v)\r\xc8\x11^L\xe1\xe3\x88~\x00*\x031\xda3\xf3o\x9c\x93 \xf2\xad\x94V\xad\xeaC\xb6\xf6\x82\xd6\x1a*5\xe8\xe5V\xd0\xcb#\x0fVz\x88{Bw}\xee<COP\xe2\xd6\xad[\x9f"\xe1\x9f\x8a\x1eq0\xee<#\xd4\x8b\x10\xe5\xd6\x83V?\xf4\xd6J\xcb\x87\xac\xb6\x17\x95\xcb\xb8\xd5S\xf5\xa3\xbe^O\xb6\xae\xd6V\xe4[{3\xcf\xd7\xf8\xb6\x92\xe7\xcb\xad\xc7=\x9f\xfbh\xc1\xff\x99\xcb\xc8\x89yY\x9e\xb7\xc2\xf3\x8fU\xd4\xfb?\xff\x96[\x86\xd6\xb1\xd99\xa9m\xf97GU\xf9\xb7V\xfc<\x10\xf9V\x90\xad\xad \xf2\x11\xac\xc8#\x0f\xa2<\xf2\xa0\xe7i\xd4\xfc\x7f\x8aJ\x8f=\x14=\xb0\x8c\xdc\x8a<A\x02\xaf\xae?\x8a%^\x10\xa1R\x83V\x0eY\r\xaa\x9e\xa5W\xdf\x83\xca\xe5\xdc\xea\x19\xf1\xbd\xd7\xeb\xe9\xf5\xb7zg\xfaz\xf9L}\xc4\xe3[C\x9f+\xff\x93\xff\xe5\x83S\x84\xff{\r!\xff\xc0\xafIx\x01i\xa0\xec\xff\x86\xa7\xfc?\xf7\xb9\t"\xdf\n\xb6\xfa\x90\xad\xbd\xa0\xba\x86(\xf7\x82\x91<\xf2\xc0\xd6\xbc\x07\xa3\xde\x0bF\x87\x03\xf4\xe0!\xe4V\x84\xf7f}\x97\xe8q\x07\xe3\n\xfd?s+B\x94[\x0fZ\xfd\xd0[C\xe4Yz\xf5=\xa9\\\xde\xad\x9e\xaa\x1f\xf5\xf5z\xb2u\xb5V\xc9A\xd7#\xc7\xce\xd4\xad\xc7\xd7Y\xf1\xaa\xf9o_-\xeb\x0c\xdf\x82\x80\xfcC\xfc\xb1\x9d\xef\xbfZ\x1d~\x90-\xdar\xcb\x12\x1d\xdb;\xdf\xa5\xde\x92A\xe4{A\xcf\x83\xea\x1a*5\xe8\xe5V\xd0\xcb#\x0f|\xae1\xf2\xe0\xbbg\x86\x03\xf4\x04\xc3\xc8\xad\x08\xcfd\xfd\x03\xd1\xd3\x0e\xc6\x9d\xff3\xfb\x08\x99\x07\x95\x1c\xfc\x1a\xaa\x9e\xa5W\xdf\x93\xcae\x9e\xf5D\xb5Y/[\xaf\xa8\xad\xc8g\xea\xd6\xe3{\xde\xbeA\x06\x84/#\x19\xc6\x9eh\x18\x19\x92\'I\xf8N\x11o\x8b\xd7Mg7\xdf\xa8\x076\x87\xac\x06U\xcf\xd2\xab\x9f\x82\xdee\xdf\xaa\x8f\xf8\xde\xeb\xf5\xf4\xfa\xab\xbd\xab\xf3\x99:\x91\xbf\x9c\xf6<\x19\x8e_88\x13L\xdd\xc5R\xe4\x1f\xe6o\x8a\xfc\x07R\xa3\xea]\x98\x99\xbb:+\xee\x1eA\xe4\x9fZ\x10\xf9*\xd8\xeaC\xb6\xf6\x1e\xb4j~\r\xb6f\x05+\xf2\xc8\x03[\xf3\x1eh\xfc\xf7[\x86\x03\xf4D\xd3\xc8\xad\x08o\x83\xe7V\xe4),\xf1\x92\x08[r\xf0k\xa8z\x96^\xfd\x14\xf4.\xff\xac\x1e\xd5f\xbd\x91\xf5\x8aZ/\xdf\xdaK\xe4\xfd\x83_#\x03\xc2\x17\x90LcO>\x8d\x0c\xc9\x93%\xfcs\xd1\x87\x1e\x8c;\x9b\xcfG\xd8\x92\x83_C\xd5\xb3\xf4\xea\xa7\xa2w\x1dd\xf5\xa86\xeb\x8d\xac\xab\xb5\xd1c*\xc7V\x8ec(\xbe^\x86c\xe8E\xc1\x08{\xe2M\xc8\x90<G\xc2_\x15qN\xbb\xf94\xf7\x11*9\x8c\xae!\xf2\x94\xacv\x1d\xf4\xae\x87\xac\x1e\xd5*\xdehO\xef\xf8V\xef\xea\xbc\xd2\xfb\xcfd8\xf4Y\xd6M\xd8\x93n\xe2\xf8\xac\xd6\xb7\x89\x9ey0\xeelB\x1f!\xf3\x94V\xcd\xf7A\xd5S\xb2Z\x8b\xea1[.\xd3\xec\xd8\xd1Z\xc5\xeb\xf5\xf4\xfa\xab\xbd{\xe6\xde\xe3\xadP\xdf(\x03\xc2+\xe7\x9b\xb1\'\xdf\x8c\x0c\xc9\xc7H\xe0\xe3\xb9|LW7\x94\x8f\x10\xe5\xd6\x83V?\xf4\xd6\x10yJV\xf3\x8c\xf4zf.\xdf\xec\x98\xd1Z\xc5[\xb9n\xe5P\xe9\x1b\xc9#\x8f/]\xffs2\x1c\xbc\xdbc\t\xf6\x1fY\x82\x0c\xc9\xe7J\xf8\xc7"\xff\x8e_\xd0<\xf2\xa0\x92\x83_C\xd5S\xb2\xda\x08\x9cg\xe5\xe5\xd8;W\xab>\xe2{o\xe5\xba\x95C\xa5\xaf\x97\xb7\xea|\xbe\xe3\xaf\xc9p\xe8\xf7J/\xc1\xfe\x03\xcb\x90!\xf9*\t\x7f\xe5ju\xd7F\xd4<\xf2\xa0\x95CV\x83\xaa\xa7d\xb5\x88\xd1\xfe-\x97m\xef\xd8V\xbd\xeaG}\xbd\x9el\xbd\xb5V\xe9o\xf5h\xfe\x1d2\x1c\xff\xee\x98/\xc3\xff0K\x90\x01\xe1\xf5\x8a\xbf-\xfa\xe3\x07\xe3\xce\xe6\xb2\x9b,\xf3\x94j\r\xfc\x1a"O\xc9j\x9e\x91\xde\x88\x99\xcb\xb9wL\xab\x1e\xf9\xb3^\xb6^Q\xab\x1cS\xe9\xff\xef\xa2o\x96\x01)}Jp\x04\xffC-C\x86\x8474\xfe\x13\xd1\xa7\xb3\xc43\x11\xa2\xdco\xc4V?\xf4\xd6\x10y\xd0\xf2#Fz+\x8c\\\xe6\xbd\xdeV=\xf2+^\xaf\xa7\xd7_\xed]\x99\xf3G\xff\xf9\x10\xd4[\x0e\xceb\xec?\xb6\x1c\x19\x12>;\xf2/D\x1fw0\xee\xdel[r\xf0k\xa8zJV\x8b\x18\xedWf/\xe7\xdeq\xad\xfa\x88\xef\xbd\x95\xebV\x0e\x95\xbe^\xceWR\xf1z\x07\xdf#\xbd\x0b\xf6\x1f\xdd\x05\x19\x92O\x93\xf0\x1d\xa2\x0f?\x18w6\x99\xddl\x95\x1c\xb2\x1aT=%\xabY\xaa}\x15F/\xf3^\x7f\xab^\xf5\xa3\xbe^O\xb6^Q\xab\xe4\xbc\xcf\x8a[\x0e\xde\x8c\xb8\x1b\xf6\x1f\xdc\r\x19\x92/\x90\xf0\x0fE\xf6S\x88\xa0y\xe4\x81\xdf\x98Y\r\xaa\x1e\xb4|O\xb5o\x94\xd1\xcb>\xebo\xd5"\x7f\xd6\x1bYWk\xb3\xc7\xf0\xd9\xf2o\x91\xe1\xf8\xb1\x83\xb3#\xfe\x87\xda\r\x19\x92/\x97\xf0\xcd"}\xfa\x17\xec\xe6\x1b\xcd\xa1\xb7\x86\xc8\x83\x96o\xa9\xf4le\xe4:\xc8z[\xb5\xc8\xafx\xa3=\xbd\xe3[\xbd\xa39\x0f\xc4\xff\x91\xe8\x07d@v\xbf~\xec?\xbc+2 \xfc[\x7fF\xf4\x8d\xa2\x0f\xc2\x13\xec/8\x9a\x83_C\xd5\x83\x96\x1f1\xd2[a\xf4\xb2\xef\xf5g\xf5\xa8V\xf1F{V\xd4\xb2\x9c\xefg\xe3=\x7f\xdf+\xc3\xd1\xfc\x93\x05+\xb1?\xc0\xee\x1c\x87\xe4\xabE\xdf \xe2\xa9`\xbb\xe9Fs\xf0k\xa8z\xd0\xf2=\xd5\xbe\x19F\xaf\x83\xac\xbfU\x1b\xf1\xbd\xd7\xeb\xe9\xf5W{{9\xd7\x01_\x16\xf2/O5\x1c\xe0\x7f\xe0\x93 \x83\xf2\x17$\xfc%\x91\x1d\x12\xbb\t\xfd\x86l\xd5|\x1fT=h\xf9\x96J\xcf*\xaa\xd7G\xd6\xd7\xaa\x8d\xf8\xde[\xb9n\xe5\x90\xd5\xbe[\xc4\x9b\x10Oy}\xdc\xf3C\x9c\x0c\x19\x92\xaf\x95\xf0\x97Ezw\x0b\xf4\x97\xb7\x17\x82\xbf@F\xd7\x10y\xd0\xf2-\x95\x9e\x95T\xaf\x93\xac\xafU\xab\xfaQ_\xaf\'[o\xa9qk\xc1-\xc7w\x9ez8\xc0\xffp\'\xe3xw\xeb+E\x7f]\xc4\x87\xae\xc0^\x00\x95\x1czke\xd4\xf7T\xfb\xb60r}\xf4z[\xf5\xc8\xafx\xa3=\xbd\xe3[\xbd6\xe7\x019\xaf\xa3}\xcf)\xefVY\xfc\x0f}R\x8eC\xf2,\xd1\xdf\x14\xd9?\xd0\x03\xad\x1c\xb2\x1aT=h\xf9\x96J\xcfJ\xaa\xd7K\xaf\xafU\x8f\xfc\x8a\xd7\xeb\xe9\xf5W{\xc9y*\xf7\xdbE<[u-\xc3\x01\xfe\x87\xbc\x16dP\xf8\x0c\xc9\xdf\x17\xe9\x8b\x89`7\xa5\xdf\xa0\xa3k\x88<h\xf9\x96J\xcfj\xaa\xd7M\xaf/\xaa\xb7\x8e\xa9\xf4\xae\\\xb7j\xbc\x08\xf8\xad\xa2\xffz\x1dw\xab,\xfe\x07\xbc6dHx\xcf\x16\xff\xc7\x88\xde\x96\x02v\xdd\xca\x95\xaa\x07-_\xe9\xd5\xf7\xa6z\x1de}Q\xad\xd5\xef\xfd\xca\xb1#\xeb^\xed7E\x7fC\x06\xe3\x15\x07\xe7\x9a\xf1?\xec\xb5"C\xf2D\t\xbc\xe2n\xdf\xe0\xa8\xd8uV\x83hSG\x1e\xb4|\xa5W?\x15\x95\xeb*\xeb\x89j\xad~\xefW\x8e\xdd\xb2\xd6\x9co \xf9&\x19\x8e\xe1\xaf\x08\xdd\x0b\xffC_;2$\x8f\x91\xf0-\xa2?q0\xee`7\xaa\xdf\xb4\xbd5d\x1b=\xab)\x95\x9e\xbd\xa8^OY_\xab\x16\xf9\x15o\xa6\xc7\xae}\x8d\xbf\xc9\xffm2\x1cS\xdf\x80\xb8\x17\xd1/y\xed\xc8\x90\xf0\xfa\xc8\xd7\x88\xf8\xd0U\xf4\xc9D\xb0\xebh\xf3f\xfd\x9e\xac\x06\xbd\xfa)\xa8^WY_\xab\x16\xf9\x15o\xb4\'\xaa\xf1`\x9c\xaf\x8d\xfa\xb72\x1c\xcb?\xcf\xb1\x95\xe8\x17<\x1bdP\x9e!\xe1\xef\x8a\xf8\x8c;\xd8\x8d\xda\x1b\x80hSW=O\xa5\xe7TT\xae\xb3\xac\xa7U\x8b\xfc\x8a\xd7\xeb\xc9\xfa\xf9\x0c\xf9\xb7\xca`\xf0\x17g\xcf\x92\xe8\x97;+dH>V\xc2\xdf\x12}\xe1\xc1\xb8Co \xaa\xc3\xd0\xdb\xfc\xbd\xfauP\xb9\xde\xb2\x9eV-\xf2+\xde\xe8\x1a\xf8\xec\xf8\xdf\x91\xe1x\xfd\xd5\xf2<\x89~\xf0\xb3C\x86\x84\xd7H\xf4s\xee\xfe\xcb\xe9\x94\xde\x1aZ\x9b\xbd2\x04\x95\x9eSQ\xb9\xde\xb2\x9eV-\xf2g\xbd\xd6\x9a/u\xe3\xf3A\xfc!\xcd\xa9/\x94>%\xd1/z\xb6\xc8\xa0\xf0\xec\x16w\xb9>\xf5`\xdc\xbdi\xab\x03Q\xf5,\xbd\xfauP\xb9\xee\xb2\x9eV-\xf2+^\xa5\x87\xaf\x03\xe5.\xd5\xff\xb9Z\x9e?\xd1/u\xd6\xc8\x90|\xb0\x84\xaf\x13=O\xc4\xb7\xca[\xfcF\xee\xad\x95K\x1c\x10\xa8\\\x7fYO\xab\x16\xf9\x15\xaf\xd5\xf3n\xd1\xf7\x8a\xfe\xb5\x0c\x07/\x02^\x0c\xd1/t\x11\xc8\xa0\xf0\x17wyl\xf2\xf9"\xfd=*\x03Q\xf5,\xb3\x03R=n\xeb\xf5\xd0;>\xab\xb7j\x91_\xf1\xfc\x9a?\xb9\xfc\xf7d0^u\xb5\xbc,Z\x17\xceEp|l\xc2{\xb9xW0\xaf\xc0W6\x7fk\xd3\xf66su\xb3\x9f\x9a\xcau\x98\xf5\xb4jU?\xea\xc3{\x93\x88o\xd9\xfc\x8f2\x1c\x9b\xbea\xfd:i]\x08\x17\x85\x0c\xcaGJ\xf8\xf3\xa2\xe7\x8a\xf8\xdc\xbbR\x19\x18\xe5R\x07D\xa9\\\x97\xad\x9e\xad\xbe]\xf3\xba\xc6\x0f\x88\xbeK\x06\x83\xa7q/\x9a\xd6\x05p\x91\xc8\xa0\xf0\x17\xaf\xbeI\xf4E\xa2\xca\x0b\x8c\x96\xbd\x06d\xe4\xb8\xad\xd7G\xe5\xf8V\xcf\x88\x1fy\xbc\xc8\xf7b\xd1\xb7\xcb`\xbc\xfa\xe0\xdc\x07T.\xd0\x8bC\x06\xe5\xb3%|\xbd\x88w\t\xdb\x0fd)\xd1\xa6\xcd6\xf2\xe8p\xcc\x0e\x93g\xe6\xfa\xa9\x1c\xd3\xea\x19\xf1\xd5c0\xf8\x03\xfd\xbc\x1a\xfe\xd32\x1c\xab~\xf7\xb3\xa0ra^$2$\xfcn\x9f\'z\xbe\xe8\xe9\xa2\xe8\x93\x8b\x9e\xde\x95\xbb\xea\xca\xb7\xe7Y}\x1dT\xce\x97\xf5D\xb5\xc8\xe33\x1a?%b0^*\x83qm\x9f\xd9\xd8\x93\xd5W\xce\xd9!\x83\xc2`|\x96\x88\xf7v}\x89\xc8\x7f0\xcb\xb2\xc7\x80\xcc\x0e\xd5\x96\xeb\xa6rl\xd6\x13\xd5\xd4\xe3\x16\x83\xef\xc2\xfd>\xd1+d0x\xccq\xdf\xb2\xe5J\xb8(\x8e\xb7(\x9f \xe2\xb3\xf0<\xf3\xc5w\x07{\xb2\xcd<\xba\xd1g\x07#b\xe6z\xaa\x1c\x93\xf5\xf8\xda;E/\x14}\x8f\xe8\x97\xee\xb7\xbbR-f.\xf8\x8bG\x86\xe5\xb1\x12\xfe\xa4\xe8\xd9\xa2\xcf\x10\xb5\x1e\xd0[F6\xc4^\x9bg\x8fA\xc9\xea\xdcZ\xf0\xe5\xd0/\x10\xfd\x88\x0c\xc5oa>H<\x90\x03\xa2\xc8\xa0\xf0\xb6\xfa\xa7\x8a\xbeB\xf4\xc5"\xfd4cDu\xd3\x9f\xea\xff\xac#\xd7\xdd\xe8\x90\xfc\x86\xe8E\xa2\x1f\x16q7\xea\xbe||Q\xe1\x81\x1e\x10\x8b\x0c\x0b\x9f\x87\xff\x1c\xd1\x97\x89x\xe70\x7fN\xce3\xba\xf9\xf7\x18\x96\x99\xeb\xac2 \xdc:\xfc\x84\x88\xbbQ<\x1b\xf5\x0e\x89\x0f<7\x03\x12 \xc3\xc2;\x86y\x06\xec\x8f\x89\x18\x16\x1e\xbb\xf8o\x82\xec\xb1\xf7-\xc9\xe8u\xe7\xfb\xb9Ux\x83\x88\xa1\xf8q\xd1\xcbd(\xde%\xf1\x06\xc3\xcd\x80\x14\x90\x81\xf9d\t\xbc\xa6\xc2\x07\xb8\xb8K\xf6Q"\xfd.\xaf\x88S\xdd\xcd\x82\xeau\xc8\xb3M|\x9c\x95\xbf\x1d\xfe\x93">\xa4\xf4\x8b\x0f\xca\x83\xedYn\x06d\x10\x19\x16\x06\xe3\x93D\x0c\n\x7f\xb0\xf43E\xfc\xa1 \x1e\xf8\x8f\xde\xca\xac\xc4^\x97\xfc\x0co\x15\xf1\xd7^_)\xe2\r\x83?#\xfae\x19\x88\xb3\xff\x0c\xc69q3 \x1b\x91\x81\xe12\xe4\x8b&\x1e\'z\x8a\x88?\x18\xc4[^\xf8\x86\x96\x8f>\xca\xbe?l%\xfc-p\x1e;\xf0\xc6@\xee.\xbdV\xf4s"\xbe\x1d\x84\xaf\xcfy\xeb\xcd-\xc46n\x06d\'dp\xb85a0\x10\x1f\x1b\xe6n\x19o\xaa\xb4_\x8e7\x03\x8f\x13\xf8{|\xaf\x13\xbd]\xc4;e\xdf+\x83\xf0\xc0>\xd3\xb4\x1f\x0f{\xd8\xff\x07\xce%\x81x\x82\xdbX\xec\x00\x00\x00\x00IEND\xaeB`\x82'  # NOQA
ui_img_gradient = lv.img_dsc_t(
    {'data_size': len(ui_img_gradient), 'data': ui_img_gradient}  # NOQA
)

_style = lv.style_t()
_style.init()  # NOQA

_style.set_bg_color(lv.color_hex(0x000000))  # NOQA
_style.set_bg_opa(0)  # NOQA
_style.set_border_color(lv.color_hex(0x000000))  # NOQA
_style.set_border_opa(0)  # NOQA
_style.set_border_width(0)  # NOQA
_style.set_margin_bottom(0)  # NOQA
_style.set_margin_left(0)  # NOQA
_style.set_margin_right(0)  # NOQA
_style.set_margin_top(0)  # NOQA
_style.set_outline_color(lv.color_hex(0x000000))  # NOQA
_style.set_outline_opa(0)  # NOQA
_style.set_outline_pad(0)  # NOQA
_style.set_outline_width(0)  # NOQA
_style.set_pad_left(0)  # NOQA
_style.set_pad_right(0)  # NOQA
_style.set_pad_top(0)  # NOQA
_style.set_pad_bottom(0)  # NOQA
_style.set_radius(0)  # NOQA
_style.set_shadow_color(lv.color_hex(0x000000))  # NOQA
_style.set_shadow_opa(0)  # NOQA
_style.set_shadow_spread(0)  # NOQA
_style.set_shadow_width(0)  # NOQA
_style.set_shadow_ofs_x(0)  # NOQA
_style.set_shadow_ofs_y(0)  # NOQA


def _build_gradient(begin_rgb, end_rgb, nb):
    def rgb2hex(r, g, b):
        return (r & 0xFF) << 16 | (g & 0xFF) << 8 | (b & 0xFF)

    br, bg, bb = begin_rgb
    er, eg, eb = end_rgb

    r_diff = er - br
    g_diff = eg - bg
    b_diff = eb - bb

    r_fact = r_diff / float(nb)
    g_fact = g_diff / float(nb)
    b_fact = b_diff / float(nb)

    for i in range(0, nb + 1):
        yield rgb2hex(
            fround(br + (i * r_fact)),
            fround(bg + (i * g_fact)),
            fround(bb + (i * b_fact))
        )


def _remap(value, old_min, old_max, new_min, new_max):
    return fround(
        (((value - old_min) * (new_max - new_min)) / (
                    old_max - old_min)) + new_min
        )


def fround(value):
    value = int(value * 10.0 + 0.5)
    return int(value / 10)


def _point_on_circle(degree, center_x, center_y, radius):
    radians = math.radians(degree)
    x = int(center_x + (radius * math.cos(radians)))
    y = int(center_y + (radius * math.sin(radians)))
    return x, y


def _get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def _get_angle(x1, y1, x2, y2):
    return math.degrees(math.atan2(y1 - y2, x1 - x2))


class _tick(lv.line):

    def __init__(self, parent):
        super().__init__(parent)
        self._points = None
        self._major = False

    @property
    def is_major(self):
        return self._major

    @is_major.setter
    def is_major(self, value):
        self._major = value

    def set_points(self, points, length):
        self._points = points
        super().set_points(points, length)

    def get_points(self):
        return self._points

    @property
    def length(self):
        if self._points is None:
            raise RuntimeError('this should not happen, sanity check')

        p1, p2 = self._points

        return _get_distance(p1.x, p1.y, p2.x, p2.y)

    @property
    def angle(self):
        if self._points is None:
            raise RuntimeError('this should not happen, sanity check')

        p1 = self._points[0]

        return math.degrees(math.atan2(p1.y, p1.x))


class knob_ctrl(lv.obj):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().add_style(_style, 0)
        super().add_flag(lv.obj.FLAG.OVERFLOW_VISIBLE)

        parent.update_layout()
        size = min(parent.get_width(), parent.get_height())
        size -= 20

        super().set_width(size)
        super().set_height(size)
        super().clear_flag(lv.obj.FLAG.SCROLLABLE)
        super().set_align(lv.ALIGN.CENTER)

        shadow_size = int(round(size * 0.7))

        self._shadow = shadow = lv.obj(self)
        shadow.set_width(shadow_size)
        shadow.set_height(shadow_size)
        shadow.add_style(_style, 0)
        shadow.set_style_radius(int(round(shadow_size / 2)), 0)
        shadow.set_align(lv.ALIGN.CENTER)
        shadow.set_style_shadow_opa(175, 0)
        # shadow.set_style_shadow_color(lv.color_hex(0x7F7F7F), 0)

        shadow.set_style_shadow_width(60, 0)
        shadow.set_style_shadow_spread(2, 0)
        shadow.set_style_shadow_ofs_x(-20, 0)
        shadow.set_style_shadow_ofs_y(-20, 0)
        shadow.clear_flag(lv.obj.FLAG.SCROLLABLE)
        shadow.clear_flag(lv.obj.FLAG.CLICKABLE)

        self._glow = glow = lv.obj(self)
        glow.set_width(shadow_size)
        glow.set_height(shadow_size)
        glow.set_align(lv.ALIGN.CENTER)
        glow.clear_flag(lv.obj.FLAG.SCROLLABLE)
        glow.clear_flag(lv.obj.FLAG.CLICKABLE)
        glow.add_style(_style, 0)
        glow.set_style_bg_opa(255, 0)

        glow.set_style_radius(int(shadow_size / 2), 0)
        glow.set_style_shadow_color(lv.color_hex(0xFF0000), 0)
        glow.set_style_shadow_opa(255, 0)
        glow.set_style_shadow_width(40, 0)
        glow.set_style_shadow_spread(5, 0)

        ring_img_size = _remap(shadow_size, 0, 200, 0, 256)

        self._ring_img = ring_img = lv.img(glow)
        ring_img.set_src(ui_img_gradient)
        ring_img.set_width(lv.SIZE_CONTENT)  # NOQA
        ring_img.set_height(lv.SIZE_CONTENT)  # NOQA
        ring_img.set_align(lv.ALIGN.CENTER)
        ring_img.clear_flag(lv.obj.FLAG.CLICKABLE)
        ring_img.clear_flag(lv.obj.FLAG.SCROLLABLE)
        ring_img.set_style_img_recolor(lv.color_hex(0x646464), 0)
        ring_img.set_style_img_recolor_opa(255, 0)
        ring_img.set_zoom(ring_img_size)

        indent_size = int(shadow_size * 0.7)

        self._indent = indent = lv.obj(self)
        indent.set_width(indent_size)
        indent.set_height(indent_size)
        indent.set_align(lv.ALIGN.CENTER)
        indent.clear_flag(lv.obj.FLAG.SCROLLABLE)
        indent.clear_flag(lv.obj.FLAG.CLICKABLE)
        indent.add_style(_style, 0)

        indent.set_style_radius(int(indent_size / 2), 0)
        indent.set_style_bg_color(lv.color_hex(0x000000), 0)
        indent.set_style_bg_opa(255, 0)

        self._indent_img = indent_img = lv.img(indent)
        indent_img.set_src(ui_img_gradient)
        indent_img.set_width(lv.SIZE_CONTENT)  # NOQA
        indent_img.set_height(lv.SIZE_CONTENT)  # NOQA
        indent_img.set_align(lv.ALIGN.CENTER)
        indent_img.clear_flag(lv.obj.FLAG.SCROLLABLE)
        indent_img.clear_flag(lv.obj.FLAG.CLICKABLE)

        indent_img.set_angle(1800)
        indent_img_size = _remap(indent_size, 0, 151, 0, 194)
        indent_img.set_zoom(indent_img_size)

        indent_img.set_style_img_recolor(lv.color_hex(0x646464), 0)
        indent_img.set_style_img_recolor_opa(255, 0)

        knob_size = int(((shadow_size - indent_size) / 2) * 0.6)
        self._start_angle = 135
        self._stop_angle = 405

        self._knob_r = knob_r = (
            (((shadow_size - indent_size) / 2) + indent_size) / 2
        )

        self._knob_glow = knob_glow = lv.obj(self)

        knob_glow.set_width(knob_size)
        knob_glow.set_height(knob_size)
        knob_glow.set_align(lv.ALIGN.CENTER)

        knob_x, knob_y = _point_on_circle(self._start_angle, 0, 0, knob_r)

        knob_glow.set_x(knob_x)
        knob_glow.set_y(knob_y)
        knob_glow.clear_flag(lv.obj.FLAG.SCROLLABLE)
        knob_glow.add_style(_style, 0)

        knob_glow.set_style_radius(int(knob_size / 2), 0)

        knob_glow.set_style_bg_opa(255, 0)
        knob_glow.set_style_shadow_color(lv.color_hex(0xFF0000), 0)
        knob_glow.set_style_shadow_opa(255, 0)
        knob_glow.set_style_shadow_width(5, 0)
        knob_glow.set_style_shadow_spread(2, 0)

        self._knob_img = knob_img = lv.img(knob_glow)
        knob_img.set_src(ui_img_gradient)
        knob_img.set_width(lv.SIZE_CONTENT)  # NOQA
        knob_img.set_height(lv.SIZE_CONTENT)  # NOQA
        knob_img.set_x(-1)
        knob_img.set_y(-1)
        knob_img.set_align(lv.ALIGN.CENTER)
        knob_img.clear_flag(lv.obj.FLAG.SCROLLABLE)
        knob_img.set_angle(1800)

        img_size = _remap(knob_size, 0, 16, 0, 21)
        knob_img.set_zoom(img_size)
        knob_img.set_style_img_recolor(lv.color_hex(0x646464), 0)
        knob_img.set_style_img_recolor_opa(255, 0)

        knob_glow.add_event_cb(
            self.__drag_event_handler,
            lv.EVENT.PRESSING,
            None
        )
        knob_img.add_event_cb(
            self.__drag_event_handler,
            lv.EVENT.PRESSING,
            None
        )
        self._captured = False

        disp = lv.disp_t.__cast__(None)  # NOQA
        self._disp_width = disp.get_hor_res()
        self._disp_height = disp.get_ver_res()

        self._snap_angles = False
        self._synchronize_glow = True
        self._scale_ticks = None
        self._scale_major_ticks = None

        self._min_value = 0
        self._max_value = 100
        self._value = -1
        self._increment = 0.01
        self._ticks = []

        self.set_scale_ticks(101, 2, 5)
        self.set_scale_major_ticks(5, 2, 11)

        grad_dsc = lv.grad_dsc_t()
        grad_dsc.stops_count = 2

        stop1 = lv.gradient_stop_t()
        stop2 = lv.gradient_stop_t()

        stop1.color = lv.color_hex(0x00FF00)
        stop2.color = lv.color_hex(0xFF0000)

        stop1.frac = int(255 * 0.7)
        stop2.frac = 255

        grad_dsc.stops = [stop1, stop2]

        self._tick_match_value = True

        self.set_style_bg_grad(grad_dsc, lv.PART.TICKS)
        self.set_value(self._min_value)

    def get_tick_match_value(self):
        return self._tick_match_value

    def set_tick_match_value(self, value):
        self._tick_match_value = value
        self.__set_knob(self._value)

    def get_synchronize_glow(self):
        return self._synchronize_glow

    def set_synchronize_glow(self, value):
        self._synchronize_glow = value
        self.__set_knob(self._value)

    def get_min_value(self):
        return self._min_value

    def set_min_value(self, value):
        self._min_value = value
        self.__set_knob(self._value)

    def get_max_value(self):
        return self._max_value

    def set_max_value(self, value):
        self._max_value = value
        self.__set_knob(self._value)

    def set_range(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self.__set_knob(self._value)

    def get_value(self):
        return self._value

    def set_value(self, value):
        remainder = value % self._increment

        if remainder < self._increment / 2:
            value -= remainder
        else:
            value += self._increment - remainder

        self._value = value
        self.__set_knob(value)

    def get_snap_angles(self):
        return self._snap_angles

    def set_snap_angles(self, value):
        self._snap_angles = value
        self.__set_knob(self._value)

    def get_increment(self):
        return self._increment

    def set_increment(self, value):
        self._increment = value
        self.__set_knob(self._value)

    def get_start_angle(self):
        return self._start_angle

    def set_start_angle(self, value):
        self._start_angle = value

    def get_stop_angle(self):
        return self._stop_angle

    def set_stop_angle(self, value):
        self._stop_angle = value

    def set_angles(self, start, stop):
        self._start_angle = start
        self._stop_angle = stop

    def set_scale_ticks(self, count, line_width, length):
        if count == 0:
            self._scale_ticks = None
            for i, tick in enumerate(self._ticks):
                if tick is None or tick.is_major:
                    continue

                tick._del()
                self._ticks[i] = None
            return

        else:
            self._scale_ticks = (count, line_width, length)

        width = self.get_width()
        height = self.get_height()

        center_x = int(width / 2)
        center_y = int(height / 2)

        size = min(width, height)
        angle_range = self._stop_angle - self._start_angle
        angle_increment = angle_range / (count - 1)

        outer_radius = (size / 2) - 4
        inner_radius = outer_radius - length

        ticks = []

        for i in range(count):
            angle = self._start_angle + i * angle_increment

            x1, y1 = _point_on_circle(angle, center_x, center_y, outer_radius)

            if len(self._ticks) - 1 >= i:
                tick = self._ticks[i]
                if tick is None:
                    tick = _tick(self)
                    x2, y2 = _point_on_circle(
                        angle,
                        center_x,
                        center_y,
                        inner_radius
                    )

                    tick.set_style_line_width(line_width, 0)

                elif tick.is_major:
                    x2, y2 = _point_on_circle(
                        angle,
                        center_x,
                        center_y,
                        outer_radius - tick.length
                    )

                else:
                    x2, y2 = _point_on_circle(
                        angle,
                        center_x,
                        center_y,
                        inner_radius
                    )
                    tick.set_style_line_width(line_width, 0)
            else:
                tick = _tick(self)

                x2, y2 = _point_on_circle(
                    angle,
                    center_x,
                    center_y,
                    inner_radius
                )

                tick.set_style_line_width(line_width, 0)

            tick.set_style_line_rounded(True, 0)
            tick.set_points(
                [lv.point_t(dict(x=x1, y=y1)), lv.point_t(dict(x=x2, y=y2))],
                2
            )
            ticks.append(tick)

        for tick in self._ticks:
            if tick is None:
                continue

            if tick not in ticks:
                tick.delete()

        self._ticks.clear()
        self._ticks.extend(ticks[:])

    def set_scale_major_ticks(self, increment, line_width, length):
        width = self.get_width()
        height = self.get_height()

        center_x = int(width / 2.0)
        center_y = int(height / 2.0)

        if increment == 0:
            self._scale_major_ticks = None

            for i, tick in enumerate(self._ticks):
                if tick is None or not tick.is_major:
                    continue

                if self._scale_ticks is None:
                    tick._del()
                else:
                    line_width, length = self._scale_ticks[1:]
                    p1, p2 = tick.get_points()

                    x1 = p1.x
                    y1 = p1.y
                    x2 = p2.x
                    y2 = p2.y
                    outer_radius = _get_distance(x1, y1, center_x, center_y)
                    inner_radius = outer_radius - length
                    angle = _get_angle(x1, y1, x2, y2)
                    x2, y2 = _point_on_circle(
                        angle,
                        center_x,
                        center_y,
                        inner_radius
                        )
                    tick.set_style_line_width(line_width, 0)
                    tick.set_points(
                        [lv.point_t(dict(x=x1, y=y1)),
                         lv.point_t(dict(x=x2, y=y2))],  # NOQA
                        2
                    )

            if self._scale_ticks is None:
                self._ticks.clear()

            return

        self._scale_major_ticks = (increment, line_width, length)

        size = min(width, height)

        outer_radius = (size / 2.0) - 4
        inner_radius = outer_radius - length

        angle_range = self._stop_angle - self._start_angle
        angle_increment = angle_range / (len(self._ticks) - 1)

        for i in range(0, len(self._ticks), increment):
            tick = self._ticks[i]

            angle = self._start_angle + i * angle_increment

            x1, y1 = _point_on_circle(angle, center_x, center_y, outer_radius)
            x2, y2 = _point_on_circle(angle, center_x, center_y, inner_radius)

            tick.set_style_line_width(line_width, 0)
            tick.set_points(
                [lv.point_t(dict(x=x1, y=y1)), lv.point_t(dict(x=x2, y=y2))],
                # NOQA
                # NOQA
                2
            )  # NOQA
            tick.is_major = True

    def __set_knob(self, value):
        if self._max_value > self._min_value:
            value_range = self._max_value - self._min_value
            modifier = self._min_value
        elif self._min_value > self._max_value:
            value_range = self._min_value - self._max_value
            modifier = self._max_value
        else:
            raise RuntimeError('min and max values should not match')

        angle_range = self._stop_angle - self._start_angle

        value_step = value_range / self._increment
        angle_step = angle_range / value_step

        value_factor = (value - modifier) / value_range

        angle_offset = angle_range * value_factor

        if self._snap_angles:
            remainder = angle_offset % angle_step
            if remainder > angle_step / 2:
                angle_offset = int(angle_offset / angle_step) + 1
            else:
                angle_offset = int(angle_offset / angle_step)

            angle = angle_offset * angle_step
        else:
            angle = angle_offset

        angle += self._start_angle

        x, y = _point_on_circle(angle, 0, 0, self._knob_r)

        if self._synchronize_glow:
            tick_num = int(round(len(self._ticks) * value_factor))

            if tick_num < len(self._ticks):
                tick = self._ticks[tick_num]
                color = tick.get_style_line_color(0)
                self._knob_glow.set_style_shadow_color(color, 0)
                self._glow.set_style_shadow_color(color, 0)

        if self._tick_match_value:
            tick_num = int(round(len(self._ticks) * value_factor))
            for i, tick in enumerate(self._ticks):
                if i <= tick_num:
                    tick.set_style_line_opa(255, 0)
                else:
                    tick.set_style_line_opa(0, 0)

        self._knob_glow.set_x(x)
        self._knob_glow.set_y(y)

    def __drag_event_handler(self, _):
        indev = lv.indev_get_act()

        point = lv.point_t()
        indev.get_point(point)  # NOQA

        knob_x1 = self.get_x() + self._knob_glow.get_x()
        knob_y1 = self.get_y() + self._knob_glow.get_y()
        knob_x2 = knob_x1 + self._knob_glow.get_x()
        knob_y2 = knob_y1 + self._knob_glow.get_y()

        hit_offset = int(self._knob_glow.get_x() * 0.4)

        knob_x1 -= hit_offset
        knob_y1 -= hit_offset

        knob_x2 += hit_offset
        knob_y2 += hit_offset

        if not knob_x1 < point.x < knob_x2:
            return
        if not knob_y1 < point.y < knob_y2:
            return

        x = point.x - self._disp_width + int(round(self._disp_width / 2))
        y = point.y - self._disp_height + int(round(self._disp_height / 2))

        if self._max_value > self._min_value:
            value_range = self._max_value - self._min_value
            min_value = self._min_value
            max_value = self._max_value
        elif self._min_value > self._max_value:
            value_range = self._min_value - self._max_value
            min_value = self._max_value
            max_value = self._min_value
        else:
            raise RuntimeError('min and max values should not match')

        angle_range = self._stop_angle - self._start_angle
        angle = math.degrees(math.atan2(y, x))

        if angle < 0:
            angle += 360

        angle_offset = angle - self._start_angle
        angle_factor = angle_offset / angle_range

        if angle_factor < 0:
            angle += 360

            angle_offset = angle - self._start_angle
            angle_factor = angle_offset / angle_range

        value = (value_range * angle_factor) + min_value

        if value < min_value:
            return
        elif value > max_value:
            return
        else:
            remainder = value % self._increment

            if remainder < self._increment / 2:
                value -= remainder
            else:
                value += self._increment - remainder

        self._value = value

        self.__set_knob(self._value)
        lv.event_send(self, lv.EVENT.VALUE_CHANGED, None)

    def __set_sizes(self):
        self.update_layout()

        width = self.get_width()
        height = self.get_height()
        size = min(width, height)

        shadow_size = int(size * 0.7)
        # img_size = _remap(size, 0, 250, 0, 256)
        ring_img_size = _remap(shadow_size, 0, 200, 0, 256)

        indent_size = int(shadow_size * 0.7)
        indent_img_size = _remap(indent_size, 0, 151, 0, 194)
        knob_size = int(((shadow_size - indent_size) / 2) * 0.6)
        knob_img_size = _remap(knob_size, 0, 16, 0, 21)

        self._knob_r = knob_r = (
            (((shadow_size - indent_size) / 2) + indent_size) / 2
        )
        knob_x, knob_y = _point_on_circle(self._start_angle, 0, 0, knob_r)

        self._knob_glow.set_x(knob_x)
        self._knob_glow.set_y(knob_y)

        self._shadow.set_width(shadow_size)
        self._shadow.set_height(shadow_size)
        self._shadow.set_style_radius(int(shadow_size / 2), 0)

        self._glow.set_width(shadow_size)
        self._glow.set_height(shadow_size)
        self._glow.set_style_radius(int(shadow_size / 2), 0)

        self._indent.set_width(indent_size)
        self._indent.set_height(indent_size)
        self._indent.set_style_radius(int(indent_size / 2), 0)

        self._knob_glow.set_width(knob_size)
        self._knob_glow.set_height(knob_size)
        self._knob_glow.set_style_radius(int(knob_size / 2), 0)

        # self._ticks_img.set_zoom(img_size)
        self._ring_img.set_zoom(ring_img_size)
        self._indent_img.set_zoom(indent_img_size)
        self._knob_img.set_zoom(knob_img_size)

    def set_style_bg_color(self, color, selector):
        if selector | lv.PART.KNOB == selector:
            selector ^= lv.PART.KNOB
            self._indent.set_style_bg_color(color, selector)
            self._glow.set_style_bg_color(color, selector)

        elif selector | lv.PART.TICKS == selector:
            selector ^= lv.PART.TICKS

            for tick in self._ticks:
                tick.set_style_line_color(color, selector)

            # self._ticks_img.set_style_img_recolor(color, selector)

        elif selector | LV_PART_KNOB_CENTER == selector:
            selector ^= LV_PART_KNOB_CENTER
            self._indent.set_style_bg_color(color, selector)

        elif selector | LV_PART_KNOB_RING == selector:
            selector ^= LV_PART_KNOB_RING
            self._glow.set_style_bg_color(color, selector)

        elif selector | lv.PART.INDICATOR == selector:
            selector ^= lv.PART.INDICATOR
            self._knob_glow.set_style_bg_color(color, selector)

        else:
            super().set_style_bg_color(color, selector)

    def set_style_bg_opa(self, opa, selector):
        if selector | lv.PART.KNOB == selector:
            selector ^= lv.PART.KNOB
            self._indent.set_style_bg_opa(opa, selector)
            self._glow.set_style_bg_opa(opa, selector)

        elif selector | lv.PART.TICKS == selector:
            selector ^= lv.PART.TICKS

            for tick in self._ticks:
                tick.set_style_line_opa(opa, selector)

            # self._ticks_img.set_style_img_recolor_opa(opa, selector)

        elif selector | LV_PART_KNOB_CENTER == selector:
            selector ^= LV_PART_KNOB_CENTER
            self._indent.set_style_bg_opa(opa, selector)

        elif selector | LV_PART_KNOB_RING == selector:
            selector ^= LV_PART_KNOB_RING
            self._glow.set_style_bg_opa(opa, selector)

        elif selector | lv.PART.INDICATOR == selector:
            selector ^= lv.PART.INDICATOR
            self._knob_glow.set_style_bg_opa(opa, selector)

        else:
            super().set_style_bg_opa(opa, selector)

    def set_style_bg_grad_color(self, color, selector):
        if selector | lv.PART.KNOB == selector:
            selector ^= lv.PART.KNOB
            self._indent_img.set_style_img_recolor(color, selector)
            self._ring_img.set_style_img_recolor(color, selector)

        elif selector | lv.PART.TICKS == selector:
            raise NotImplementedError

        elif selector | LV_PART_KNOB_CENTER == selector:
            selector ^= LV_PART_KNOB_CENTER
            self._indent_img.set_style_img_recolor(color, selector)

        elif selector | LV_PART_KNOB_RING == selector:
            selector ^= LV_PART_KNOB_RING
            self._ring_img.set_style_img_recolor(color, selector)

        elif selector | lv.PART.INDICATOR == selector:
            selector ^= lv.PART.INDICATOR
            self._knob_img.set_style_img_recolor(color, selector)

        else:
            super().set_style_bg_grad_color(color, selector)

    def set_style_bg_main_stop(self, *args, **kwargs):
        raise NotImplementedError

    def set_style_bg_grad_stop(self, *args, **kwargs):
        raise NotImplementedError

    def set_style_bg_grad(self, grad_desc, selector):
        gradient = []
        last_color = None
        for i in range(grad_desc.stops_count):
            stop = grad_desc.stops[i]
            color = stop.color
            color = (color.ch.red, color.ch.green, color.ch.blue)

            if last_color is not None:
                frac = stop.frac / 255
                num_steps = len(self._ticks) * frac
                gradient.extend(
                    list(
                        lv.color_hex(color)
                        for color in
                        _build_gradient(last_color, color, num_steps)
                    )
                )

            last_color = color

        if selector | lv.PART.TICKS == selector:
            selector ^= lv.PART.TICKS
            for i, tick in enumerate(self._ticks):
                tick.set_style_line_color(gradient[i], selector)
        else:
            raise NotImplementedError

    def set_style_bg_dither_mode(self, *args, **kwargs):
        raise NotImplementedError

    def set_style_bg_grad_dir(self, value, selector):
        if selector | lv.PART.KNOB == selector:
            selector ^= lv.PART.KNOB
            self._indent_img.set_angle(value)
            self._ring_img.set_angle(value)

        elif selector | lv.PART.TICKS == selector:
            raise NotImplementedError

        elif selector | LV_PART_KNOB_CENTER == selector:
            selector ^= LV_PART_KNOB_CENTER
            self._indent_img.set_angle(value)

        elif selector | LV_PART_KNOB_RING == selector:
            selector ^= LV_PART_KNOB_RING
            self._ring_img.set_angle(value)

        elif selector | lv.PART.INDICATOR == selector:
            selector ^= lv.PART.INDICATOR
            self._knob_img.set_angle(value)

    def set_style_outline_color(self, color, selector):
        if selector | lv.PART.KNOB == selector:
            selector ^= lv.PART.KNOB
            self._indent.set_style_outline_color(color, selector)
            self._glow.set_style_outline_color(color, selector)

        elif selector | lv.PART.TICKS == selector:
            selector ^= lv.PART.TICKS
            for tick in self._ticks:
                tick.set_style_outline_color(color, selector)

            # self._ticks_img.set_style_img_recolor(color, selector)

        elif selector | LV_PART_KNOB_CENTER == selector:
            selector ^= LV_PART_KNOB_CENTER
            self._indent.set_style_outline_color(color, selector)

        elif selector | LV_PART_KNOB_RING == selector:
            selector ^= LV_PART_KNOB_RING
            self._glow.set_style_outline_color(color, selector)

        elif selector | lv.PART.INDICATOR == selector:
            selector ^= lv.PART.INDICATOR
            self._knob_glow.set_style_outline_color(color, selector)

        else:
            self._glow.set_style_outline_color(color, selector)

    def set_style_outline_width(self, value, selector):
        if selector | lv.PART.KNOB == selector:
            selector ^= lv.PART.KNOB
            self._glow.set_style_outline_width(value, selector)

        elif selector | lv.PART.TICKS == selector:
            selector ^= lv.PART.TICKS

            for tick in self._ticks:
                tick.set_style_outline_width(value, selector)

        elif selector | LV_PART_KNOB_CENTER == selector:
            selector ^= LV_PART_KNOB_CENTER
            self._indent.set_style_outline_width(value, selector)

        elif selector | LV_PART_KNOB_RING == selector:
            selector ^= LV_PART_KNOB_RING
            self._glow.set_style_outline_width(value, selector)

        elif selector | lv.PART.INDICATOR == selector:
            selector ^= lv.PART.INDICATOR
            self._knob_glow.set_style_outline_width(value, selector)

        else:
            self._glow.set_style_outline_width(value, selector)

    def set_style_outline_opa(self, opa, selector):
        if selector | lv.PART.KNOB == selector:
            selector ^= lv.PART.KNOB
            self._indent.set_style_outline_opa(opa, selector)
            self._glow.set_style_outline_opa(opa, selector)

        elif selector | lv.PART.TICKS == selector:
            selector ^= lv.PART.TICKS

            for tick in self._ticks:
                tick.set_style_outline_opa(opa, selector)

            # self._ticks_img.set_style_img_recolor_opa(opa, selector)

        elif selector | LV_PART_KNOB_CENTER == selector:
            selector ^= LV_PART_KNOB_CENTER
            self._indent.set_style_outline_opa(opa, selector)

        elif selector | LV_PART_KNOB_RING == selector:
            selector ^= LV_PART_KNOB_RING
            self._glow.set_style_outline_opa(opa, selector)

        elif selector | lv.PART.INDICATOR == selector:
            selector ^= lv.PART.INDICATOR
            self._knob_glow.set_style_outline_opa(opa, selector)

        else:
            self._glow.set_style_outline_opa(opa, selector)

    def set_style_border_color(self, color, selector):
        if selector | lv.PART.KNOB == selector:
            selector ^= lv.PART.KNOB
            self._indent.set_style_border_color(color, selector)
            self._glow.set_style_border_color(color, selector)

        elif selector | lv.PART.TICKS == selector:
            selector ^= lv.PART.TICKS
            for tick in self._ticks:
                tick.set_style_border_color(color, selector)

            # self._ticks_img.set_style_img_recolor(color, selector)

        elif selector | LV_PART_KNOB_CENTER == selector:
            selector ^= LV_PART_KNOB_CENTER
            self._indent.set_style_border_color(color, selector)

        elif selector | LV_PART_KNOB_RING == selector:
            selector ^= LV_PART_KNOB_RING
            self._glow.set_style_border_color(color, selector)

        elif selector | lv.PART.INDICATOR == selector:
            selector ^= lv.PART.INDICATOR
            self._knob_glow.set_style_border_color(color, selector)

        else:
            self._glow.set_style_border_color(color, selector)

    def set_style_border_opa(self, opa, selector):
        if selector | lv.PART.KNOB == selector:
            selector ^= lv.PART.KNOB
            self._indent.set_style_border_opa(opa, selector)
            self._glow.set_style_border_opa(opa, selector)

        elif selector | lv.PART.TICKS == selector:
            selector ^= lv.PART.TICKS

            for tick in self._ticks:
                tick.set_style_border_opa(opa, selector)

            # self._ticks_img.set_style_img_recolor_opa(opa, selector)

        elif selector | LV_PART_KNOB_CENTER == selector:
            selector ^= LV_PART_KNOB_CENTER
            self._indent.set_style_border_opa(opa, selector)

        elif selector | LV_PART_KNOB_RING == selector:
            selector ^= LV_PART_KNOB_RING
            self._glow.set_style_border_opa(opa, selector)

        elif selector | lv.PART.INDICATOR == selector:
            selector ^= lv.PART.INDICATOR
            self._knob_glow.set_style_border_opa(opa, selector)

        else:
            self._glow.set_style_border_opa(opa, selector)

    def set_style_border_width(self, value, selector):
        if selector | lv.PART.KNOB == selector:
            selector ^= lv.PART.KNOB
            self._glow.set_style_border_width(value, selector)

        elif selector | lv.PART.TICKS == selector:
            selector ^= lv.PART.TICKS

            for tick in self._ticks:
                tick.set_style_border_width(value, selector)

        elif selector | LV_PART_KNOB_CENTER == selector:
            selector ^= LV_PART_KNOB_CENTER
            self._indent.set_style_border_width(value, selector)

        elif selector | LV_PART_KNOB_RING == selector:
            selector ^= LV_PART_KNOB_RING
            self._glow.set_style_border_width(value, selector)

        elif selector | lv.PART.INDICATOR == selector:
            selector ^= lv.PART.INDICATOR
            self._knob_glow.set_style_border_width(value, selector)

        else:
            self._glow.set_style_border_width(value, selector)

    def set_style_shadow_width(self, value, selector):
        if selector | lv.PART.KNOB == selector:
            selector ^= lv.PART.KNOB
            self._glow.set_style_shadow_width(value, selector)

        elif selector | lv.PART.TICKS == selector:
            selector ^= lv.PART.TICKS

            for tick in self._ticks:
                tick.set_style_shadow_width(value, selector)

        elif selector | LV_PART_KNOB_CENTER == selector:
            raise NotImplementedError

        elif selector | LV_PART_KNOB_RING == selector:
            selector ^= LV_PART_KNOB_RING
            self._glow.set_style_shadow_width(value, selector)

        elif selector | lv.PART.INDICATOR == selector:
            selector ^= lv.PART.INDICATOR
            self._knob_glow.set_style_shadow_width(value, selector)

        else:
            self._shadow.set_style_shadow_width(value, selector)

    def set_style_shadow_ofs_x(self, value, selector):
        if selector | lv.PART.KNOB == selector:
            selector ^= lv.PART.KNOB
            self._glow.set_style_shadow_ofs_x(value, selector)

        elif selector | lv.PART.TICKS == selector:
            selector ^= lv.PART.TICKS

            for tick in self._ticks:
                tick.set_style_shadow_ofs_x(value, selector)

        elif selector | LV_PART_KNOB_CENTER == selector:
            raise NotImplementedError

        elif selector | LV_PART_KNOB_RING == selector:
            selector ^= LV_PART_KNOB_RING
            self._glow.set_style_shadow_ofs_x(value, selector)

        elif selector | lv.PART.INDICATOR == selector:
            selector ^= lv.PART.INDICATOR
            self._knob_glow.set_style_shadow_ofs_x(value, selector)

        else:
            self._shadow.set_style_shadow_ofs_x(value, selector)

    def set_style_shadow_ofs_y(self, value, selector):
        if selector | lv.PART.KNOB == selector:
            selector ^= lv.PART.KNOB
            self._glow.set_style_shadow_ofs_y(value, selector)

        elif selector | lv.PART.TICKS == selector:
            selector ^= lv.PART.TICKS

            for tick in self._ticks:
                tick.set_style_shadow_ofs_y(value, selector)

        elif selector | LV_PART_KNOB_CENTER == selector:
            raise NotImplementedError

        elif selector | LV_PART_KNOB_RING == selector:
            selector ^= LV_PART_KNOB_RING
            self._glow.set_style_shadow_ofs_y(value, selector)

        elif selector | lv.PART.INDICATOR == selector:
            selector ^= lv.PART.INDICATOR
            self._knob_glow.set_style_shadow_ofs_y(value, selector)

        else:
            self._shadow.set_style_shadow_ofs_y(value, selector)

    def set_style_shadow_spread(self, value, selector):
        if selector | lv.PART.KNOB == selector:
            selector ^= lv.PART.KNOB
            self._glow.set_style_shadow_spread(value, selector)

        elif selector | lv.PART.TICKS == selector:
            selector ^= lv.PART.TICKS

            for tick in self._ticks:
                tick.set_style_shadow_spread(value, selector)

        elif selector | LV_PART_KNOB_CENTER == selector:
            raise NotImplementedError

        elif selector | LV_PART_KNOB_RING == selector:
            selector ^= LV_PART_KNOB_RING
            self._glow.set_style_shadow_spread(value, selector)

        elif selector | lv.PART.INDICATOR == selector:
            selector ^= lv.PART.INDICATOR
            self._knob_glow.set_style_shadow_spread(value, selector)

        else:
            self._shadow.set_style_shadow_spread(value, selector)

    def set_style_shadow_color(self, color, selector):
        if selector | lv.PART.KNOB == selector:
            selector ^= lv.PART.KNOB
            self._glow.set_style_shadow_color(color, selector)

        elif selector | lv.PART.TICKS == selector:
            selector ^= lv.PART.TICKS

            for tick in self._ticks:
                tick.set_style_shadow_color(color, selector)

        elif selector | LV_PART_KNOB_CENTER == selector:
            raise NotImplementedError

        elif selector | LV_PART_KNOB_RING == selector:
            selector ^= LV_PART_KNOB_RING
            self._glow.set_style_shadow_color(color, selector)

        elif selector | lv.PART.INDICATOR == selector:
            selector ^= lv.PART.INDICATOR
            self._knob_glow.set_style_shadow_color(color, selector)

        else:
            self._shadow.set_style_shadow_color(color, selector)

    def set_style_shadow_opa(self, opa, selector):
        if selector | lv.PART.KNOB == selector:
            selector ^= lv.PART.KNOB
            self._glow.set_style_shadow_opa(opa, selector)

        elif selector | lv.PART.TICKS == selector:
            selector ^= lv.PART.TICKS

            for tick in self._ticks:
                tick.set_style_shadow_opa(opa, selector)

        elif selector | LV_PART_KNOB_CENTER == selector:
            raise NotImplementedError

        elif selector | LV_PART_KNOB_RING == selector:
            selector ^= LV_PART_KNOB_RING
            self._glow.set_style_shadow_opa(opa, selector)

        elif selector | lv.PART.INDICATOR == selector:
            selector ^= lv.PART.INDICATOR
            self._knob_glow.set_style_shadow_opa(opa, selector)

        else:
            self._shadow.set_style_shadow_opa(opa, selector)

    def set_style_width(self, value, selector):
        raise NotImplementedError

    def set_style_height(self, value, selector):
        raise NotImplementedError

    def set_width(self, value):
        self.update_layout()
        self.set_size(value, self.get_height())

    def set_height(self, value):
        self.update_layout()
        self.set_size(self.get_height(), value)

    def set_size(self, width, height):
        super().set_size(width, height)
        self.__set_sizes()

        if self._scale_ticks is not None:
            self.set_scale_ticks(*self._scale_ticks)

        if self._scale_major_ticks is not None:
            self.set_scale_major_ticks(*self._scale_major_ticks)


if __name__ == '__main__':
    from display_driver_utils import driver

    drv = driver(width=351, height=350)

    screen = lv.scr_act()
    screen.set_style_bg_color(lv.color_hex(0x2D2D2D), 0)
    screen.set_style_bg_opa(255, 0)

    volume = knob_ctrl(screen)
    volume.set_size(200, 200)
    volume.center()
