df=read.csv('/Users/prakritsinha/Desktop/ht_data')
head(df)

#plot(x=df$Mean_Temperature_F,y=df$crime_count)
df

model1=lm(crime_count~Mean_Temperature_F,data=df)
summary(model1)

anova(model1)

plot(model1)


plot(x=df$Mean_Temperature_F,y=df$crime_count)
