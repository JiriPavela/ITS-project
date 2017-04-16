## Test Cases:
The following list contains the test cases details. All the test cases can also be found in the appropriate [Git directory](https://github.com/JiriPavela/ITS-project/tree/master/Cases). All tests expect the tester to be logged in the administration section, more precisely in the *Products* tab. The term *Products lists* refers to the list of products present in the *Products* tab in administration section. The term *Store* refers to the actual OpenCart website with products and not the administration section.
 * *1. shouldFilterQuantity0SamsungTablet*
   * **Given** a product *Samsung Galaxy Tab 10.1* in the products database
   * **And** it's parameter *Quantity* equals to *0*
   * **When** filtering criteria in *Quantity* input is set to *0*
   * **And** the *Filter* button is pressed
   * **Then** only the product *Samsung Galaxy Tab 10.1* is shown in the product list
 * *2. shouldFilterPrice80NikonCamera*
   * **Given** a product *Nikon D300* in the products database
   * **And** it's parameter *Price* equals to *80.0000*
   * **When** filtering criteria in *Price* input is set to *80*
   * **And** the *Filter* button is pressed
   * **Then** only the product *Nikon D300* is shown in the product list
 * *3. shouldFilterStatusDisabledNoResults*
   * **Given** no product with parameter *Status* set to *Disabled*
   * **When** filtering criteria in *Status* input is set to *Disabled*
   * **And** the *Filter* button is pressed
   * **Then** no product is shown in the product list and message *No results!* is shown instead
 * *4. shouldFilterProductNameSonyVAIO*
   * **Given** a product with parameter *Product Name* equal to *Sony VAIO* in the products database
   * **When** filtering criteria in *Product Name* input is set to *Sony VAIO*
   * **And** the *Filter* button is pressed
   * **Then** only the product *Sony VAIO* is shown in the product list
 * *5. shouldFilterModelProduct18MacBookPro*
   * **Given** a product *MacBook Pro* in the products database
   * **And** it's parameter *Model* equals to *Product 18*
   * **When** filtering criteria in *Model* input is set to *Product 18*
   * **And** the *Filter* button is pressed
   * **Then** only the product *MacBook Pro* is shown in the product list
 * *6. shouldAddPalmTreoProSpecial*
   * **Given** a product *Palm Treo Pro* in the products database
   * **And** the product has no special offer set in *Edit Product -> Special*
   * **When** a *Special* offer is set in *Edit Product -> Special -> Add Special* with only the *Price* parameter set to *249.9999*
   * **And** the *Save* button is pressed
   * **Then** the new *Special* offer price *249.9999* is shown in the product list for product *Palm Treo Pro* displayed with a red text
 * *7. shouldAddHPLP3065SpecialNotNumber*
   * **Given** a product *HP LP3065* in the products database
   * **And** the product has no special offer set in *Edit Product -> Special*
   * **When** a *Special* offer is set in *Edit Product -> Special -> Add Special* with only the *Price* parameter set to *nan*
   * **And** the *Save* button is pressed
   * **Then** the new *Special* offer price *0.0000* is shown in the product list for product *HP LP3065* displayed with a red text
 * *8. shouldAddHTCTouchHDSpecialNegative* 
   * **Given** a product *HTC Touch HD* in the products database
   * **And** the product has no special offer set in *Edit Product -> Special*
   * **When** a *Special* offer is set in *Edit Product -> Special -> Add Special* with only the *Price* parameter set to *-100.0*
   * **And** the *Save* button is pressed
   * **Then** the new *Special* offer price *-100.0000* is shown in the product list for product *HTC Touch HD* displayed with a red text
 * *9. shouldAddPalmTreoProDiscount2Pieces*
   * **Given** a product *Palm Treo Pro* in the products database
   * **And** the product has no *Discount* set in *Edit Product -> Discount*
   * **When** a *Discount* is set in *Edit Product -> Discount -> Add Discount* with *Quantity* set to *2* and *Price* to *229.9999*
   * **And** the *Save* button is pressed
   * **Then** the new *Discount* package for *2* pieces is displayed in the product detail in *Store* for product *Palm Treo Pro*
 * *10. shouldAddiPodShuffleDiscount0*
   * **Given** a product *iPod Shuffle* in the products database
   * **And** the product has no *Discount* set in *Edit Product -> Discount*
   * **When** a *Discount* is set in *Edit Product -> Discount -> Add Discount* with *Quantity* set to *0* and *Price* to *20*
   * **And** the *Save* button is pressed
   * **Then** no *Discount* package is displayed in the product detail in *Store* for product *iPod Shuffle*
 * *11. shouldRemoveAppleCinemaDiscount20Pieces*
   * **Given** a product *Apple Cinema 30"* in the products database
   * **And** the product has a *Discount* in *Edit Product -> Discount* for *20 pieces*
   * **When** the *Discount* for *20 pieces* is removed by clicking the *Remove* button in *Edit Product -> Discount* specification
   * **And** the *Save* button is pressed
   * **Then** the product *Apple Cinema 30"* will have no *Discount* for *20 pieces* displayed in the product detail in *Store* for product *Apple Cinema 30"*
 * *12. shouldRemoveAppleCinemaSpecial*
   * **Given** a product *Apple Cinema 30"* in the products database
   * **And** the product has one *Special* offer set in *Edit Product -> Special*
   * **When** the *Special* offer is removed from the product specification by clicking the *Remove* button
   * **And** the *Save* button is pressed
   * **Then** the product *Apple Cinema 30"* has no more a *Special offer* displayed as a red text in the product list
 * *13. shouldEditiMacQuantityTo1000*
   * **Given** a product *iMac* in the products database
   * **And** the product has a *Quantity* parameter value different from *1000*, as shown in the product list
   * **When** the *Quantity* value is set to *1000* in the *Edit Product -> Data*
   * **And** the *Save* button is pressed
   * **Then** the product *iMac* has the *Quantity* value set to *1000* in the product list
 * *14. shouldEditiPodNanoQuantityTo-10*
   * **Given** a product *iPod Nano* in the products database
   * **And** the product has a *Quantity* parameter value different from *-10*, as shown in the product list
   * **When** the *Quantity* value is set to *-10* in the *Edit Product -> Data*
   * **And** the *Save* button is pressed
   * **Then** the product *iPod Nano* has the *Quantity* value set to *-10* in the product list
 * *15. shouldEditSamsungTabletOutOfStockStatus*
   * **Given** a product *Samsung Galaxy Tab 10.1* in the products database
   * **And** the product has a *Quantity* parameter value equal to *0*, as shown in the products list
   * **And** the product has a *Out of Stock Status* parameter with value different from *Out of Stock* in the *Edit Product -> Data*
   * **When** the *Out of Stock Status* value in *Edit Product -> Data* is set to *Out of Stock*
   * **And** the *Save* button is pressed
   * **Then** the product *Samsung Galaxy Tab 10.1* now has the *Out of Stock* message displayed in the product detail in *Store*
 * *16. shouldEditiPhonePriceTo150*
   * **Given** a product *iPhone* in the products database
   * **And** the product has a *Price* parameter value different from *150.0000*, as shown in the products list
   * **When** the *Price* value is set to *150.0000* in the *Edit Product -> Data*
   * **And** the *Save* button is pressed
   * **Then** the product *iPhone* is now priced for *150.0000* in the product list
 * *17. shouldAddProductAligatorPhone*
   * **Given** no product *Aligator Phone* in the products database
   * **When** the product *Aligator Phone* is added to the existing products by clicking the *Add New* button with *General -> Product Name* set to *Aligator Phone* and *General -> Meta Tag Title* set to *Aligator Phone* and *Data -> Model* set to *Model 1*
   * **And** the button *Save* is clicked
   * **Then** the product *Aligator Phone* is present in the products list
 * *18. shouldCopyProduct8*
   * **Given** the product *Product 8* in the products database
   * **When** the product *Product 8* is marked by checking the checkbox and *Copy* button is pressed
   * **Then** the product *Product 8* is twice in the products list
 * *19. shouldRemoveProductMacBook*
   * **Given** the product *MacBook* in the products database
   * **When** the product *MacBook* is marked by checking the checkbox and *Delete* button is pressed
   * **Then** the product *MacBook* is no longer in the products list
