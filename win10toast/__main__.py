from win10toast import ToastNotifier
import time

# #############################################################################
# ###### Stand alone program ########
# ###################################
if __name__ == "__main__":
    # Example
    toaster = ToastNotifier()
    toaster.show_toast(
        "You have entered an invalid address!",
        "Please check for any errors",
        duration=10)
#     toaster.show_toast(
#         "Example two",
#         "This notification is in it's own thread!",
#         icon_path=None,
#         duration=5,
#         threaded=True
#         )
    # Wait for threaded notification to finish
    while toaster.notification_active(): time.sleep(0.1)
