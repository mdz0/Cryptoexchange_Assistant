###################################################################
###################################################################
###██╗░░░░░████████╗███╗░░██╗░██████╗░░░░█████╗░██╗░░██╗░█████╗░###
###██║░░░░░╚══██╔══╝████╗░██║██╔════╝░░░██╔══██╗╚██╗██╔╝██╔══██╗###
###██║░░░░░░░░██║░░░██╔██╗██║╚█████╗░░░░██║░░██║░╚███╔╝░██║░░██║###
###██║░░░░░░░░██║░░░██║╚████║░╚═══██╗░░░██║░░██║░██╔██╗░██║░░██║###
###███████╗░░░██║░░░██║░╚███║██████╔╝██╗╚█████╔╝██╔╝╚██╗╚█████╔╝###
###╚══════╝░░░╚═╝░░░╚═╝░░╚══╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░###
###################################################################
###################################################################

# mail:ltns.0x0@gmail.com

import uvicorn


if __name__ == "__main__":
    uvicorn.run("api.api:app", host="0.0.0.0", port=5438, reload=True)