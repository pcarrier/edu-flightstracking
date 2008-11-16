<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
				xmlns:f="http://snibbits.net/~gcarrier/ns/tracking"
                version="1.0"
                >
 
    <xsl:output method="xml" indent="yes"/>

	<xsl:template match="/">
    	<xsl:element name="kml">
    		<xsl:element name="Document">
    			<xsl:element name="name">
    				<xsl:text>Actualité des vols</xsl:text>
    			</xsl:element>
    			<xsl:element name="description">
    				<xsl:text>Une carte des vols - cliquer sur un symbole pour voir les vols à l'arrivé en provenance de Paris, Orly</xsl:text>
    			</xsl:element>
    		
    			<xsl:apply-templates select="//f:locations"/>
    		</xsl:element>
    	</xsl:element>
    </xsl:template>
    
    
	<xsl:template match="f:locations">
	
	<xsl:for-each select="//f:location">
			<xsl:variable name="locationName"><xsl:value-of select="@name"/></xsl:variable>
    		<xsl:element name="Placemark">		
   					<xsl:element name="name"><xsl:value-of select="$locationName"/></xsl:element>
    				
    				<xsl:element name="description">
    				<xsl:if test="count(//f:flights/f:flight/f:departure[@location=$locationName])>0">
	    				<xsl:for-each select="//f:flights/f:flight/f:departure[@location=$locationName]">
							<xsl:element name="div">
							<xsl:value-of select="../@name"/>
							</xsl:element>
							
							<xsl:element name="div">
							Status :<xsl:value-of select="../@status"/>
							
							</xsl:element>
							<xsl:element name="div">
								<xsl:value-of select="@datetime"/>
								<xsl:text> </xsl:text>
								<xsl:value-of select="@location"/>
							</xsl:element>
							
							<xsl:element name="div">
								<xsl:value-of select="../f:arrival/@datetime"/>
								<xsl:text> </xsl:text>
								<xsl:value-of select="../f:arrival/@location"/>
							</xsl:element> 
	    				</xsl:for-each>
	    			</xsl:if>
	    			
	    			<xsl:if test="count(//f:flights/f:flight/f:arrival[@location=$locationName])>0">
	    				<xsl:text>
	    				Arrivées</xsl:text>
	    				<xsl:for-each select="//f:flights/f:flight/f:arrival[@location=$locationName]">
							Vol :<xsl:value-of select="../@name"/>
							Status :<xsl:value-of select="../@status"/>
							Heure de départ :<xsl:value-of select="@datetime"/>
	    				</xsl:for-each>
	    			</xsl:if>
    				</xsl:element>
    				
    				<xsl:element name="Point">
    				<xsl:element name="coordinates">
    					<xsl:value-of select="//f:coordinates"/>
    				</xsl:element>
    			</xsl:element>
    		</xsl:element>
    	</xsl:for-each>
	</xsl:template>
</xsl:stylesheet>