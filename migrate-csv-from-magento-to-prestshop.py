# coding=utf-8
import csv
import re
from datetime import datetime

#
# Steps before running the file
#   1- Copy the images from magento to prestashop.
#      rsync -avzp /[magento-root-path]/pub/media/catalog/product/ /[prestashop-root-path]/img/
#   2- Change the final domain of your store in DOMAIN
#   3- Export the magento products in System -> DataTransfer in CSV format and place the path of the downloaded file in MAGENTO_CSV_FILE_PATH.
#   4- Run the script
#   5- Import the file that I declare in PRESTASHOP_CSV_FILE_PATH in your store in prestashop.
#


# DOMAIN PRESTASHOP (for importer images)
DOMAIN = "http://www.xxx.com"
# INPUT
MAGENTO_CSV_FILE_PATH = "magento-data-test.csv"
# OUTPUT
PRESTASHOP_CSV_FILE_PATH = "prestashop-data-products.csv"

#
# ** Do not touch code from here down unless you have to change the features
#

with open(PRESTASHOP_CSV_FILE_PATH, mode='w') as file:
    w = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    w.writerow(['Product ID', 'Active (0/1)', 'Name *', 'Categories (x,y,z...)', 'Price tax excluded', 'Tax rules ID', 'Wholesale price', 'On sale (0/1)', 'Discount amount', 'Discount percent', 'Discount from (yyyy-mm-dd)', 'Discount to (yyyy-mm-dd)', 'Reference #', 'Supplier reference #', 'Supplier', 'Manufacturer', 'EAN13', 'UPC', 'Ecotax', 'Width', 'Height', 'Depth', 'Weight', 'Delivery time of in-stock products', 'Delivery time of out-of-stock products with allowed orders', 'Quantity', 'Minimal quantity', 'Low stock level', 'Send me an email when the quantity is under this level', 'Visibility', 'Additional shipping cost', 'Unity', 'Unit price', 'Summary', 'Description', 'Tags (x,y,z...)', 'Meta title', 'Meta keywords', 'Meta description', 'URL rewritten', 'Text when in stock', 'Text when backorder allowed', 'Available for order (0 = No, 1 = Yes)', 'Product available date', 'Product creation date', 'Show price (0 = No, 1 = Yes)', 'Image URLs (x,y,z...)', 'Image alt texts (x,y,z...)', 'Delete existing images (0 = No, 1 = Yes)', 'Feature(Name:Value:Position)', 'Available online only (0 = No, 1 = Yes)', 'Condition', 'Customizable (0 = No, 1 = Yes)', 'Uploadable files (0 = No, 1 = Yes)', 'Text fields (0 = No, 1 = Yes)', 'Out of stock action', 'Virtual product', 'File URL', 'Number of allowed downloads', 'Expiration date', 'Number of days', 'ID / Name of shop', 'Advanced stock management', 'Depends On Stock', 'Warehouse', 'Acessories  (x,y,z...)'])
   
    with open(MAGENTO_CSV_FILE_PATH) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        id = 0
        for row in csv_reader:
            if id > 0:

                # Product ID
                product_id = str(id + 1)
                # Active (0/1)
                active = str(row[10])
                # Name *
                name = str(row[6].replace("#",""))
                # Categories (x,y,z...)
                categories = re.split('/|,',row[4])
                cat = []
                for c in range(len(categories)):
                    category = categories[c].strip()
                    if(categories[c] == 'Default Category'):
                        category = 'Inicio'
                    if category not in cat:
                        cat.append(category)
                # Price tax excluded
                price_tax_excluded = str(row[13])
                # Tax rules ID
                tax_rules_id = ""
                # Wholesale price
                wholesale_price = ""
                # On sale (0/1)
                on_sale = "0"
                # Discount amount
                discount_amount = ""
                # Discount percent
                discount_percent = ""
                # Discount from (yyyy-mm-dd)
                discount_from = ""
                # Discount to (yyyy-mm-dd)
                discount_to = ""
                # Reference #
                reference = ""
                # Supplier reference #
                supplier_reference = ""
                # Supplier
                supplier = ""
                # Manufacturer
                manufacturer = str(row[45])
                # EAN13
                ean = ""
                # UPC
                upc = ""
                # Ecotax
                ecotax = ""
                # Width
                width = ""
                # Height
                height = ""
                # Depth
                depth = ""
                # Weight
                weight = str(row[9])
                # Delivery time of in-stock products
                delivery_time_of_in_stock_products = ""
                # Delivery time of out-of-stock products with allowed orders
                delivery_time_of_out_of_stock_products_with_allowed_orders = "" 
                # Quantity
                quantity = str(row[47].split(".")[0])
                # Minimal quantity
                minimal_quantity = str(row[53].split(".")[0])
                # Low stock level
                low_stock_level = str(row[58].split(".")[0])
                # Send me an email when the quantity is under this level
                send_me_an_email_when_the_quantity_is_under_this_level =  str(row[59])
                # Visibility
                visibility = str(row[12].lower().split(",")[0])
                # Additional shipping cost
                additional_shipping_cost = ""
                # Unity
                unity = ""
                # Unit price
                unit_price = ""
                # Summary
                summary = str(row[8])
                # Description
                description = str(row[7])
                # Tags (x,y,z...)
                tags = str(row[19])
                tags = re.split(' |,|-',tags)
                # Meta title
                meta_title = str(row[18])
                # Meta keywords
                meta_keywords = str(row[19])
                # Meta description
                meta_description = str(row[20])
                # URL rewritten
                url_rewritten = str(row[17])
                # Text when in stock
                text_when_in_stock = "In Stock" 
                # Text when backorder allowed
                text_when_backorder_allowed = "Current supply. Ordering availlable"
                # Available for order (0 = No, 1 = Yes)
                available_for_order = "1"
                # Product available date
                product_available_date = ""
                # Product creation date
                product_creation_date = str(row[29].strip().split(" ")[0])
                product_creation_date = datetime.strptime(product_creation_date, '%d/%m/%y')
                product_creation_date = product_creation_date.strftime("%Y-%m-%d")
                product_available_date = product_creation_date
                # Show price (0 = No, 1 = Yes)
                show_price = "1"
                # Image URLs (x,y,z...)
                images = str(row[74].strip())
                images = images.strip().split(",")
                images_ = []
                for i in range(len(images)):
                    images_.append(DOMAIN + "/img" + images[i])
                # Image alt texts (x,y,z...)
                image_alt_texts = ""
                # Delete existing images (0 = No, 1 = Yes)
                delete_existing_images = "0"
                # Available online only (0 = No, 1 = Yes)
                available_online_only = "0"
                # Condition
                condition = "new"
                # Customizable (0 = No, 1 = Yes)
                customizable = "0"
                # Uploadable files (0 = No, 1 = Yes)
                uploadable_files = "0"
                # Text fields (0 = No, 1 = Yes)
                text_fields = "0"
                # Out of stock action
                out_of_stoc_kaction = "0"
                # Virtual product
                virtual_product = "0"
                # File URL
                file_url = ""
                # Number of allowed downloads
                number_of_allowed_downloads = ""
                # Expiration date
                expiration_date = ""
                # Number of days
                number_of_days = ""
                # ID / Name of shop 
                ID_Name_of_shop = "0"
                # Advanced stock management
                advanced_stock_management = "0"
                # Depends On Stock
                depends_on_stock = "0"
                # Warehouse
                warehouse = "0"
                # Acessories  (x,y,z...)
                acessories = ""

                # *
                # *
                # * This section is particular, it depends on the additional features of the product.
                # *
                # *

                # Feature(Name:Value:Position)
                features = str(row[46])
                features = re.split(',',features)
                features_ = []
                pos=1
                for f in range(len(features)):
                    if "complejidad" in features[f]:
                        features_.append("Complejidad:" + str(features[f].split('=')[1]) + ":" + str(pos))
                        pos+=1
                    if "dependencia_del_idioma" in features[f]:
                        flag = "No"
                        if features[f].split('=')[1] == "Yes":
                            flag = "Si"
                        features_.append("Dependencia del idioma:" + str(flag) + ":" + str(pos))
                        pos+=1
                    if "edad=" in features[f]:
                        features_.append("Edad:" + str(features[f].split('=')[1]) + ":" + str(pos))
                        pos += 1      
                    if "edad_recomendada" in features[f]:
                        features_.append("Edad recomendada:" + str(features[f].split('=')[1]) + ":" + str(pos))
                        pos += 1
                    if "editorial" in features[f]:
                        features_.append("Editorial:" + str(features[f].split('=')[1]) + ":" + str(pos))
                        pos += 1  
                    if "idioma" in features[f]:
                        features_.append("Idioma:" + str(features[f].split('=')[1]) + ":" + str(pos))
                        pos += 1  
                    if "max_jugadores" in features[f]:
                        features_.append("Maximo de jugadores:" + str(features[f].split('=')[1]) + ":" + str(pos))
                        pos += 1  
                    if "min_jugadores" in features[f]:
                        features_.append("Minimo de jugadores :" + str(features[f].split('=')[1]) + ":" + str(pos))
                        pos += 1              
                    if "mecanica" in features[f]:
                        features_.append("Mecánica:" + str(features[f].split('=')[1]) + ":" + str(pos))
                        pos += 1             
                    if "n_de_jugadores" in features[f]:
                        features_.append("Nº de jugadores (Rango) :" + str(features[f].split('=')[1]) + ":" + str(pos))
                        pos += 1  
                    if "pais_de_origen" in features[f]:
                        features_.append("País de origen:" + str(features[f].split('=')[1]) + ":" + str(pos))
                        pos += 1   
                    if "tematica" in features[f]:
                        features_.append("Temática :" + str(features[f].split('=')[1]) + ":" + str(pos))
                        pos += 1
                    if "tiempo_de_juego" in features[f]:
                        features_.append("Tiempo de juego:" + str(features[f].split('=')[1]) + ":" + str(pos))
                        pos += 1   
                    if "ts_dimensions_height" in features[f]:
                        height = str(features[f].split('=')[1]);
                    if "ts_dimensions_length" in features[f]:
                        depth = str(features[f].split('=')[1]);
                    if "ts_dimensions_width" in features[f]:
                        width = str(features[f].split('=')[1]);
                        pos += 1  

                print("           product_id: " + product_id)
                print("                name:  " + name)
                print("")
                w.writerow([product_id, active, name, ','.join(cat), price_tax_excluded, tax_rules_id, wholesale_price, on_sale, discount_amount, discount_percent, discount_from, discount_to, reference, supplier_reference, supplier, manufacturer, ean, upc, ecotax, width, height, depth, weight, delivery_time_of_in_stock_products, delivery_time_of_out_of_stock_products_with_allowed_orders, quantity, minimal_quantity, low_stock_level, send_me_an_email_when_the_quantity_is_under_this_level, visibility, additional_shipping_cost, unity, unit_price, summary, description, ','.join(tags), meta_title, meta_keywords, meta_description, url_rewritten, text_when_in_stock, text_when_backorder_allowed, available_for_order, product_available_date, product_creation_date, show_price, ','.join(images_), image_alt_texts, delete_existing_images, ','.join(features_), available_online_only, condition, customizable, uploadable_files, text_fields, out_of_stoc_kaction, virtual_product, file_url, number_of_allowed_downloads, expiration_date, number_of_days, ID_Name_of_shop, advanced_stock_management, depends_on_stock, warehouse, acessories])
            id += 1


    

