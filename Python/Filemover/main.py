import os
import shutil

old_path = "C:\\old_path"    # Här anger man toppmappen som innehåller alla "småmappar" med många filer i.
new_path = "C:\\new_path"    # Här anger man målmappen. filerna från old_path kommer att hamna i en enda stor mapp.

def move_files(old_path):
    list_with_files = os.listdir(old_path)          # list_with_files här visar alla mappar som finns i mappen på old_path
    for file in list_with_files:                    # file första varvet kommer bli "mapp1"
        if os.path.isdir(old_path + file):          # OM det finns fler mappar i mapp1 där man befinner sig i så forstätt med if'en.
            move_files(old_path + file)             # I detta fall är det flera mappar i mappen. Därför lägger vi till filnamnet för första mappen vi hittade. I detta fall mapp1 och sedan kör vi om funktionen!
        else:                                       # Finns det inga fler mappar så kör vi else:.
            shutil.copyfile(old_path + "\\" + file, new_path + file) # Denna kopierar filen från gamla platsen till den nya.
    
move_files(old_path)