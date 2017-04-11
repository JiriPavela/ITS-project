## Test Cases:
The following list contains the test cases details.
 * *shouldFilterQuantity0SamsungTablet*
   * **Given** a product *Samsung Galaxy Tab 10.1*
   * **And** it's parameter *Quantity* equals to *0*
   * **When** products are filtered by *Quantity* set to *0*
   * **Then** only the product *Samsung Galaxy Tab 10.1* is shown in the product list
 * *shouldFilterPrice80NikonCamera*
   * **Given** a product *Nikon D300*
   * **And** it's parameter *Price* equals to *80.0000*
   * **When** products are filtered by *Price* set to *80*
   * **Then** only the product *Nikon D300* is shown in the product list
 * *shouldFilterStatusDisabledNoResults*
   * **Given** no product with parameter *Status* set to *Disabled*
   * **When** products are filtered by *Status* set to *Disabled*
   * **Then** no product is shown in the product list and message *No results!* is shown instead
 * *shouldFilterProductNameSonyVAIO*
   * **Given** a product with parameter *Product Name* equal to *Sony VAIO*
   * **When** products are filtered by *Product Name* set to *Sony VAIO*
   * **Then** only the product *Sony VAIO* is shown in the product list
 * *shouldFilterModelProduct18MacBookPro*
   * **Given** a product *MacBook Pro*
   * **And** it's parameter *Model* equals to *Product 18*
   * **When** products are filtered by *Model* set to *Product 18*
   * **Then** only the product *MacBook Pro* is shown in the product list
 * *shouldAddPalmTreoProSpecial*
   * **Given** a product *Palm Treo Pro*
   * **And** the product has no *Special* offer set in product details
   * **When** a *Special* offer is set to reduce the price to *249.9999*
   * **Then** the new *Special* offer price *249.9999* is shown in the product list
 * *shouldAddPalmTreoProDiscount2Pieces*
   * **Given** a product *Palm Treo Pro*
   * **And** the product has no *Discount* set in product details
   * **When** a *Discount* is set to reduce the price for *2 pieces* to *229.9999* per piece
   * **Then** the new *Discount* package is displayed in the product detail in *Store*
 * *shouldRemoveAppleCinemaDiscount20Pieces*
   * **Given** a product *Apple Cinema 30"*
   * **And** the product has a *Discount* for *20 pieces* set in product details
   * **When** the *Discount* for *20 pieces* is removed from the product specification
   * **Then** the product *Apple Cinema 30"* will have no *Discount* for *20 pieces* displayed in the product detail in *Store*
 * *shouldRemoveAppleCinemaSpecial*
   * **Given** a product *Apple Cinema 30"*
   * **And** the product has one *Special* offer set in product details
   * **When** the *Special* offer is removed from the product specification
   * **Then** the product *Apple Cinema 30"* has no more a *Special offer*
 * *shouldEditiMacQuantityTo1000*
   * **Given** a product *iMac*
   * **And** the product has a *Quantity* parameter value different from *1000*
   * **When** the *Quantity* value is set to *1000* in the product edit form
   * **Then** the product *iMac* is now stocked with *1000* items
 * *shouldEditiPodNanoQuantityTo-10*
   * **Given** a product *iPod Nano*
   * **And** the product has a *Quantity* parameter value different from *-10*
   * **When** the *Quantity* value is set to *-10* in the product edit form
   * **Then** the product *iPod Nano* is now stocked with *-10* items 
 * *shouldEditSamsungTabletOutOfStockStatus*
   * **Given** a product *Samsung Galaxy Tab 10.1*
   * **And** the product has a *Quantity* parameter value equal to *0*
   * **And** the product has a *Out of Stock Status* parameter with value different from *Out of Stock*
   * **When** the *Out of Stock Status* value is set to *Out of Stock* in the product edit form
   * **Then** the product *Samsung Galaxy Tab 10.1* now has the *Out of Stock* message displayed in the product detail in *Store*
 * *shouldEditiPhonePriceTo150*
   * **Given** a product *iPhone*
   * **And** the product has a *Price* parameter value different from *150.0000*
   * **When** the *Price* value is set to *150.0000* in the product edit form
   * **Then** the product *iPhone* is now priced for *150.0000* in the product list
 * *shouldAddProductAligatorPhone*
   * **Given** no product *Aligator Phone* in the products list
   * **When** the product *Aligator Phone* is added to the existing products
   * **Then** the product *Aligator Phone* is present in the products list
 * *shouldCopyProduct8*
   * **Given** the product *Product 8* in the products list
   * **When** the product *Product 8* is marked and *Copy* is performed
   * **Then** the product *Product 8* is twice in the products list
 * *shouldRemoveProductMacBook*
   * **Given** the product *MacBook* in the products list
   * **When** the product *MacBook is marked and *Delete* is performed
   * **Then** the product *MacBook* is no longer in the products list

