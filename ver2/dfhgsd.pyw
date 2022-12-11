import pystray

from PIL import Image, ImageDraw

def on_clicked(sorterTray,item):
    if str(item)=="Downloads Folder":
        print("iam download path")
    elif str(item)=="Organize":
        print("Oraganize function is running")
    elif str(item)=="Exit":
        sorterTray.stop()

def create_image(width, height, color1, color2):
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image

icon=create_image(64, 64, 'black', 'white')

sorterTray=pystray.Icon("DownloadSorter",icon,menu=pystray.Menu(
    pystray.MenuItem("Downloads Folder",on_clicked),
    pystray.MenuItem("Organize",on_clicked),
    pystray.MenuItem("Exit",on_clicked)
))

sorterTray.run()
# To finally show you icon, call run
# icon.run()