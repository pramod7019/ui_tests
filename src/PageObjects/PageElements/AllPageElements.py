from .FavPageElements import FavPageElements
from .ConfirmationPageElements import ConfirmationPageElements
from .CheckoutPageSummarySectionElements import CheckoutPageSummarySectionElements
from .ShoppingBagPageElements import ShoppingBagPageElements
from .PDPPageElements import PDPPageElements
from .PLPPageElements import PLPPageElements
from .SignInPageElements import SignInPageElements
from .HeaderPageElements import HeaderPageElements
from .CheckoutPageReviewSectionElements import CheckoutPageReviewSectionElements
from .CheckoutPageShippingSectionElements import CheckoutPageShippingSectionElements


class AllPageElements:

    PDP_PAGE_ELEMENTS = PDPPageElements()
    PLP_PAGE_ELEMENTS = PLPPageElements()
    SHOPPING_BAG_PAGE_ELEMENTS = ShoppingBagPageElements()
    SIGN_IN_PAGE_ELEMENTS = SignInPageElements()
    HEADER_PAGE_ELEMENTS = HeaderPageElements()
    CHECKOUT_PAGE_SUMMARY_SECTION_ELEMENTS = CheckoutPageSummarySectionElements()
    CHECKOUT_PAGE_REVIEW_SECTION_ELEMENTS = CheckoutPageReviewSectionElements()
    CONFIRMATION_PAGE_ELEMENTS = ConfirmationPageElements()
    CHECKOUT_PAGE_SHIPPING_SECTION_ELEMENTS = CheckoutPageShippingSectionElements()
    FAV_PAGE_ELEMENTS = FavPageElements()

