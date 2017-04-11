# Test Plan for OpenCart eCommerce System
**Author**: Jiří Pavela
**Login**: xpavel32
**Date**: April 11th, 2017

## Test Plan Identifier
TestPlan-OpenCart-Products-v1.0

## Introduction
The test plan specifies manner, in which the OpenCart system should be tested --- specifically the product management subsystem in administration interface and the expected impact of products changes on the shop products statuses. The test plan covers the general approach to the subsystem testing, tested and not tested features, assumptions and dependencies which shaped the test plan specification, various criteria for the tests success evaluation etc.

**Disclaimer.** This test plan does not address the overall functionality testing for the whole OpenCart system.

## Test Items:

The objectives of the testing:
  * OpenCart v. 2.2.0.0
    * Product management subsystem
    * The expected impacts of the subsystem changes on the shop products statuses

## Features to be Tested:

The list of features which are covered by this test plan:
  * Products list filtering
  * Product discounts and special offers
  * Product quantity behavior
  * Certain product add / change / removal in the product list

## Features Not to Be Tested:

All the other features of the OpenCart system not specified in the covered features section. The scope of the test plan is based around the product management. Different (possibly future) work may address other features functionality testing.

## Approach:

The testing is performed on the OpenCart system operations which are considered as a Black Box. The test cases themselves are designed to be automated by the Selenium IDE tool appropriate for the GUI testing. The testing is targeted only on a small subsystem, which should be tested on the surface, rather than to its depth and details.

## Item Pass/Fail Criteria:

The OpenCart testing procedure is considered as a passed if:
 * Each test case is successfully finished, i.e. none test case failed

The OpenCart testing procedure is considered as a failed if:
 * One or more test case exited with the failed status

## Suspension Criteria and Resumption Requirements:

Some test modify the shop internal database and multiple test runs without environment reset to the default state might introduce false results. 

In order to correctly re-run the test suite, the OpenCart system should be reverted back to the default state.

## Test Deliverables:

The test plan deliverables consist of:
 * The plan itself available at [Git plan directory](https://github.com/JiriPavela/ITS-project/tree/master/Plan).
 * The test cases available separately at [Git test cases directory](https://github.com/JiriPavela/ITS-project/tree/master/Cases).
 * The test scripts available at [Git scripts directory](https://github.com/JiriPavela/ITS-project/tree/master/Scripts).
 * The test logs available at [Git logs directory](https://github.com/JiriPavela/ITS-project/tree/master/Logs).

## Test Environment:

The testing environment consists of following aspects and their properties:
 * **Hardware**
   * CPU: Genuine Intel® CPU U4100 @ 1.30GHz × 2
   * GPU: Mobile Intel® GM45 Express Chipset
   * RAM: 3.8 GiB
 * **Software**
   * OS: Ubuntu 14.04 LTS, 64bit version
   * Mozilla Firefox, version 49.0
 * **Network connection**
   * 100 Mbps Optic Fiber
 * **Tools**
   * Selenium IDE 2.9.1.1

## Estimate:

The test suite is not particularly large and therefore the time requirements should be in magnitude of tens of seconds. The speed might further depend on the network connection speed.  

## Test Cases:
The following list contains the test cases details. All the test cases can also be found in the appropriate [Git directory](https://github.com/JiriPavela/ITS-project/tree/master/Cases).
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

## Risks:

Failed tests might leave the OpenCart products subsystem database in a non-defined state where e.g. certain products might or might not be in the database / updated etc. Modifications of the products subsystem other than the one produced by a test cases during testing might cause unexpected tests failures. 

## Assumptions and Dependencies:

The test procedure expects default state of the OpenCart testing environment and its database in order to successfully perform the tests. A stable network connection is also considered as a necessary prerequisite. 
