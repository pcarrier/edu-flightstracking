<?xml version="1.0"?>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
				xmlns:f="http://snibbits.net/~gcarrier/ns/tracking"
                version="1.0">

    <xsl:output method="xml" indent="yes"/>

	<xsl:template match="/">
    	<xsl:element name="kml">
    		<xsl:element name="Document">
    			<xsl:element name="name">
    				<xsl:text>Actualité des vols</xsl:text>
    			</xsl:element>
    			<xsl:element name="description">
    				<xsl:text>Une carte des vols - cliquez sur un symbole pour voir les vols à l'arrivée en provenance de Paris, Orly</xsl:text>
    			</xsl:element>
    			<xsl:apply-templates select="//f:locations"/>
    		</xsl:element>
    	</xsl:element>
    </xsl:template>
    
    
	<xsl:template match="f:locations">
	
	<xsl:for-each select="//f:location">
			<xsl:variable name="locationName"><xsl:value-of select="@name"/></xsl:variable>
    		<xsl:element name="Placemark">		
   					<xsl:element name="name"><xsl:value-of select="./f:airport/@name"/></xsl:element>
    				
    				<xsl:element name="description">
    				  
    				<xsl:choose>
	    			<xsl:when test="count(//f:flights/f:flight/f:arrival[@location=$locationName])>0">
	    			<xsl:for-each select="//f:flights/f:flight/f:arrival[@location=$locationName]">
	    				   <xsl:variable name="departureLocation" select="../f:departure/@location"/>
							<xsl:element name="div">
							<xsl:value-of select="../@name"/> :
							
							<xsl:value-of select="../@status"/>
							
							</xsl:element>
							<xsl:element name="div">
								<xsl:value-of select="../f:arrival/@datetime"/>
								<xsl:text> </xsl:text>
								<xsl:value-of select="//f:location[@name=$departureLocation]/f:airport/@city"/>,
								<xsl:value-of select="//f:location[@name=$departureLocation]/f:airport/@name"/>
								(<xsl:value-of select="//f:location[@name=$departureLocation]/f:airport/@code"/>) -
								<xsl:value-of select="//f:location[@name=$departureLocation]/f:airport/@country"/>
								
								<xsl:if test="//f:location[@name=$departureLocation]/f:gate/@name != ''">
									<xsl:text> Terminal </xsl:text>
									<xsl:value-of select="//f:location[@name=$departureLocation]/f:gate/@name"/>
								</xsl:if>
							</xsl:element>
							
							<xsl:element name="div">
								<xsl:value-of select="@datetime"/>
								<xsl:text> </xsl:text>
								<xsl:value-of select="//f:location[@name=$locationName]/f:airport/@city"/>,
								
								<xsl:value-of select="//f:location[@name=$locationName]/f:airport/@name"/>
								(<xsl:value-of select="//f:location[@name=$locationName]/f:airport/@code"/>) -
								
								<xsl:value-of select="//f:location[@name=$locationName]/f:airport/@country"/>
								
								<xsl:if test="//f:location[@name=$locationName]/f:gate/@name != ''">
									<xsl:text> Terminal </xsl:text>
									<xsl:value-of select="//f:location[@name=$locationName]/f:gate/@name"/>
								</xsl:if>
							</xsl:element>
							
	    				</xsl:for-each>
	    			</xsl:when>
	    			<xsl:otherwise>
	    			There are not flight on arrival in this airport.
	    			</xsl:otherwise>
	    			</xsl:choose>	    			
    				</xsl:element>
    		<xsl:element name="Point">
	    		<xsl:element name="coordinates">
	    			<xsl:value-of select="./f:coordinates"/>
	    		</xsl:element>
    		</xsl:element>
    		</xsl:element>

    	</xsl:for-each>
	</xsl:template>
</xsl:stylesheet>