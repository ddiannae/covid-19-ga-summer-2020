###############################################################################
#Exploratory Data Analysis 
#Extract and modify to get attack rates
#Mexican COVID19 open data
###############################################################################


###############################################################################
#read data
###############################################################################

el_path <- "http://187.191.75.115/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip"

#el_path <- 
#paste0("http://187.191.75.115/gobmx/salud/datos_abiertos/historicos/datos_abiertos_covid19_", 
#       format((Sys.Date() -2), "%d.%m.%Y"), #two day delay
#       ".zip")
#el_path <- "http://187.191.75.115/gobmx/salud/datos_abiertos/historicos/datos_abiertos_covid19_18.04.2020.zip"
temp <- tempfile()
download.file(url = el_path, destfile = temp)
el_file <- unzip(zipfile = temp, list = T)
el_file <- unz(description = temp, filename = el_file[1])
el_data <- vroom::vroom(el_file)
unlink(temp)
rm(temp, el_file)

###############################################################################
#tidy data
###############################################################################

###############################################################################
###############################################################################
#explore
###############################################################################
###############################################################################

#list variables 

my_vars <- colnames(el_data)

###

###counts cdmx
filter(ENTIDAD_RES == "09", ENTIDAD_UM == "09", RESULTADO == 1) %>%  #live and treated in CDMX
  nrow #9682
  #pull(ID_REGISTRO) %>% unique %>% length
  

grupos_edad <-
el_data %>% 
  filter(ENTIDAD_RES == "09", ENTIDAD_UM == "09") %>%  #live and treated in CDMX
  mutate(RANGO_EDAD = cut(EDAD, seq(0,120, 10), include.lowest = T) #group by ages
           ) %>% 
  group_by(RANGO_EDAD) 
# mutate(ALTA_QUINCENA_ACTUAL = (FECHA_SINTOMAS >= (Sys.Date() -15))) %>% 
#   filter(ALTA_QUINCENA_ACTUAL == T) %>% 
#   group_by(RANGO_EDAD, FECHA_SINTOMAS) %>%
#   tally() #
  # ungroup %>% 
  # #mutate(RANGO_EDAD = as.character(RANGO_EDAD)) %>% 
  # complete(RANGO_EDAD, FECHA_SINTOMAS, fill = list(n=0)) %>% 
  # ggplot(mapping = aes(x = FECHA_SINTOMAS, y = n, colour = RANGO_EDAD)) + 
  # geom_line()

  
###

### sintomas ultimos 15 dias
sintomas_quincena <-
  el_data %>% 
  filter(ENTIDAD_RES == "09", ENTIDAD_UM == "09", RESULTADO == 1) %>%  #live and treated in CDMX
  mutate(ALTA_QUINCENA_ACTUAL = (FECHA_SINTOMAS >= (Sys.Date() -15))) %>% 
  filter(ALTA_QUINCENA_ACTUAL == T) %>% 
  group_by(FECHA_SINTOMAS) %>% 
  tally() %>% 
  complete(FECHA_SINTOMAS, fill = list(n=0))

### hospitalizados ultimos 15 dias

hospit_quincena <-
  el_data %>% 
  filter(ENTIDAD_RES == "09", ENTIDAD_UM == "09", RESULTADO == 1) %>%  #live and treated in CDMX
  mutate(HOSP_QUINCENA_ACTUAL = (FECHA_INGRESO >= (Sys.Date() -15))) %>% 
  filter(HOSP_QUINCENA_ACTUAL == T) %>% 
  group_by(FECHA_INGRESO) %>% 
  tally() %>% 
  complete(FECHA_INGRESO, fill = list(n=0))

### defunciones ultimos 15 dias

defun_quincena <-
  el_data %>% 
  filter(ENTIDAD_RES == "09", ENTIDAD_UM == "09", RESULTADO == 1) %>%  #live and treated in CDMX
  mutate(DEF_QUINCENA_ACTUAL = (FECHA_DEF >= (Sys.Date() -15))) %>% 
  filter(DEF_QUINCENA_ACTUAL == T) %>% 
  group_by(FECHA_DEF) %>% 
  tally() %>% 
  complete(FECHA_DEF, fill = list(n=0))



